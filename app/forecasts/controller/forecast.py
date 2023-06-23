"""Controller for response Forecast API"""
from forecasts.models import generate_api


def get_forecast(point=None):
    forecast = generate_api.Api()
    result = None
    if point:
        result = forecast.get_forecast(point=point)
    else:
        result = forecast.get_forecast(point=None)
    return result
