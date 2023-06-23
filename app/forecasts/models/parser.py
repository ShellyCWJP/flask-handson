"""スクレイピングで取得したデータをパースするモジュール"""
from forecasts.models import convert_jp


def point_forecast(tr, date):
    """取得した要素から天気予報データを返却する
        Args:
            tr (WebElement): 取得した要素
        Returns:
            dict: 地点の1週間の天気予報データ
    """
    point_name = tr.find('th').text

    # 天気予報
    weathers = tr.findAll('td')
    weathers = list(map(lambda td: td.text, weathers))

    # 降水確率
    rain_row = tr.nextSibling
    rain = rain_row.findAll('td')
    rain = list(map(lambda td: td.text, rain))

    # 最低・最高気温
    temperature_row = rain_row.nextSibling.nextSibling
    temperature = temperature_row.findAll('td')
    temperature = list(map(lambda td: td.text, temperature))

    forecasts = []

    for i, item in enumerate(date):
        forecasts.append({
            'date': item,
            'weather': weathers[i],
            'rain': rain[i],
            'low': temperature[i].split(' / ')[0],
            'high': temperature[i].split(' / ')[1],
        })

    return {
        'id': convert_jp.kanji_romaji(point_name),
        'name': point_name,
        'forecasts': forecasts,
    }
