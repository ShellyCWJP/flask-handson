"""Define forecast model"""
import re

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from forecasts.models import parser


URL = 'https://www.jma.go.jp/bosai/forecast/'


def forecast_data(point=None):
    """Get forecast data from scraping"""

    options = Options()

    # Docker 環境下でも実行できるようにするためのオプション
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)

    driver.get(URL)

    try:
        # CSR 表示されるまで待機
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'contents-header'))
        )
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        # 更新日時を取得
        update_date = soup\
            .findAll('tr', class_='contents-header')[0].find('th').text

        # 天気予報の表
        forecast_table = soup.findAll('table', class_='forecast-table')[1]

        # すべての予報日の日付を取得
        number_pattern = r'\d+'
        date = forecast_table\
            .find('tr', class_='contents-header').findAll('th')
        date = list(map(lambda th: th.text, date))[1:]
        date = [int(num) for s in date
                for num in re.findall(number_pattern, s)]

        # すべての地点の天気予報をフォーマットする
        points = forecast_table.findAll('tr', class_='contents-bold-top')[1:]
        points = [point for point in points
                  if 'contents-header'not in point.get('class')]
        points = list(map(lambda point:
                          parser.point_forecast(point, date), points))

    finally:
        driver.quit()

    forecast_data = None

    if point is None:
        forecast_data = points
    else:
        forecast_data = list(filter(lambda p: p['id'] == point, points))

    response_data = {
        'point': point,
        'updated_at': update_date,
        'forecasts': forecast_data,
    }

    if len(forecast_data) == 0:
        return {'message': 'Point not found.'}

    return response_data
