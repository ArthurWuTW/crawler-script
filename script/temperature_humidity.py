
import requests
from bs4 import BeautifulSoup
import time
import re
import os
import urllib
import json
import io

while True:
  URL = "https://weather.com/zh-TW/weather/hourbyhour/l/ab6a0d440cf29997c96b86e11b647c285d3a489a623ea04d29fdefe0ea3534b2"
  res = requests.get(URL)
  soup = BeautifulSoup(res.text, 'html.parser')
  divs = soup.find_all("ul", {"class": "_2qH8C", "data-testid": "DetailsTable"})
  divs = divs[0].find_all("li", {"class": "_3Kt-N _23W42", "data-testid": "HumiditySection"})
  divs = divs[0].find_all("span", {"class": "_1F3Ze"})
  humidity = divs[0].string[:-1]

  divs = soup.find_all("summary", {"class": "AvowU _2nJx1 LEvZQ"})
  divs = divs[0].find_all("span", {"class": "RcZzi", "data-testid": "TemperatureValue"})
  temperature = divs[0].string[:-1]

  print(humidity, temperature)


  # Post data
  ip = 'http://10.1.1.16:8000'
  data = '/temperature/'+ temperature
  r = requests.get(ip+data)

  data = '/humidity/'+ humidity
  r = requests.get(ip+data)

  time.sleep(60*30)

