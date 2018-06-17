from HttpData import HttpData
from WeatherDataPoints import WeatherDataPoints

def main():
    http = HttpData()
    data = http.GET('https://api.darksky.net/forecast/668bf60cf034c2c299111995b6d32d81/51.5074,0.1278', 'json')
    dataPoint = WeatherDataPoints()
    dataPoint.clear_day()