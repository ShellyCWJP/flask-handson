from flask import Flask, jsonify

import forecasts.controller.forecast
from myexception import MyException, InputException

app = Flask(__name__)


@app.errorhandler(MyException)
def handle_my_exception(error):
    return jsonify({'message': error.message}), error.code


@app.route('/')
def main():
    data = forecasts.controller.forecast.get_forecast()
    return data


@app.route('/<point>')
def point(point):
    data = forecasts.controller.forecast.get_forecast(point=point)
    response = data.get_json()

    if response['res']['message']:
        raise InputException(response['res']['message'])

    return data


app.run(host='0.0.0.0', port=5000)
