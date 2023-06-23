"""Define Api format for response"""
from flask import jsonify

from forecasts.models import scraping


class Api(object):
    def __init__(self, data=None, point=None):
        self.data = data
        self.point = point

    def _api_wrapper(function):
        def wrapper(*args, **kwargs):
            data = function(*args, **kwargs)
            return jsonify({
                "res": data
            })
        return wrapper

    @_api_wrapper
    def get_forecast(self, point):
        return scraping.forecast_data(point)
