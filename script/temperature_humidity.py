
import requests
from bs4 import BeautifulSoup
import time
import re
import os
import urllib
import json
import io

while True:
  URL = "https://www.cwb.gov.tw/V8/C/W/Observe/MOD/24hr/C0V77.html"
  res = requests.get(URL)
  soup = BeautifulSoup(res.text, 'html.parser')
  divs = soup.find_all("td", {"headers": "hum"})
  humidity = divs[0].string

  divs = soup.find_all("span", {"class": "tem-C is-active"})
  temperature = divs[0].string

  print(humidity, temperature)
  ip = 'http://10.1.1.16:8000'
  try:
    check = float(temperature)
    # Post data
    data = '/temperature/'+ temperature
    r = requests.get(ip+data)
  except ValueError:
    r = requests.get(ip+'/writeLogMessage/TEMP/%5BCrawler%5D%20TEMP%20Crawler%20Failed/WARNING')
  
  try:
    check = float(humidity)
    data = '/humidity/'+ humidity
    r = requests.get(ip+data)
    #time.sleep(60*30)
  except ValueError:
    r = requests.get(ip+'/writeLogMessage/HUMID/%5BCrawler%5D%20HUMID%20Crawler%20Failed/WARNING')
  
  break
