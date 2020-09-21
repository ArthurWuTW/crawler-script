
import requests
from bs4 import BeautifulSoup
import time
import re
import os
import urllib
import json
import io

URL = "https://weather.com/zh-TW/weather/today/l/ab6a0d440cf29997c96b86e11b647c285d3a489a623ea04d29fdefe0ea3534b2"
res = requests.get(URL)
soup = BeautifulSoup(res.text, 'html.parser')
divs = soup.find_all("div", {"class": "_2h2vG"})
divs = divs[0].find_all("span", {"class": "_3KcTQ"})
temperature = float(divs[0].string[:-1])

print(temperature)



