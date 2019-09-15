"""
A module that handles acquiring all weather related content for the app.

author: Wiley Matthews.
date: 9/2/2019
"""

import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime


# API Keys
DARKSKY_KEY = 'b3f609149b1cdc25c712bba1f8c20430'  # Probably not the best idea to have my api key on github... but if it
                                                  # becomes a problem I'll deal with it then. This is good for now so
                                                  # that anyone can clone this repo and have a working demo.

# URLs
AWC_BASE_URL = 'https://www.aviationweather.gov'
AWC_PROG_PAGE = 'https://www.aviationweather.gov/progchart/sfc'
DARKSKY_HOURLY = 'https://api.darksky.net/forecast/{}/43.15,-77.68?exclude=minutely,daily,alerts,flags'.format(DARKSKY_KEY)


def get_prog():
    """
    Parses Aviation Weather center for the most current surface prognostic chart and returns the image as bytes.
    :return: bytes Prog chart image
    """
    response = requests.get(AWC_PROG_PAGE)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
    prog_img = soup.find('img', {"id": "image"})
    prog_url = AWC_BASE_URL + prog_img['src']
    return urlopen(prog_url).read()


def get_forecast():
    """
    Calls the DarkSky weather API and returns the relevant weather data.
    :return: dict current weather data, dict forecast outlook for the day, dict 10 hours of hourly forecasts
    """
    weather_data = requests.get(DARKSKY_HOURLY).json()

    current_data = {
                'time': datetime.fromtimestamp(weather_data['currently']['time']).strftime("%I:%M %p"),
                'date': datetime.fromtimestamp(weather_data['currently']['time']).strftime("%m/%d"),
                'summary': weather_data['currently']['summary'],
                'icon': weather_data['currently']['icon'],
                'precipProbability': weather_data['currently']['precipProbability'],
                'temperature': round(weather_data['currently']['temperature'])
            }

    gen_forecast = {
        'summary': weather_data['hourly']['summary'],
        'icon': weather_data['hourly']['icon']
    }

    hourly_forecast = []
    for i in range(10):
        hourly_forecast.append(
            {
                'time': datetime.fromtimestamp(weather_data['hourly']['data'][i]['time']).strftime("%I:%M %p"),
                'date': datetime.fromtimestamp(weather_data['hourly']['data'][i]['time']).strftime("%m/%d"),
                'summary': weather_data['hourly']['data'][i]['summary'],
                'icon': weather_data['hourly']['data'][i]['icon'],
                'precipProbability': weather_data['hourly']['data'][i]['precipProbability'],
                'temperature': round(weather_data['hourly']['data'][i]['temperature'])
            }
        )
    return current_data, gen_forecast, hourly_forecast
