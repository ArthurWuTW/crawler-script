
import requests
from bs4 import BeautifulSoup
import time
import re
import os
import urllib
import json
import io
import json
import os
secret_data_path = os.path.dirname(os.path.abspath(__file__))+"/secret_data.json"
secret_data = None
with open(secret_data_path, "r") as file:
    secret_data = json.load(file)
print(secret_data)

while True:
  URL = "https://www.cwb.gov.tw/V8/C/W/Observe/MOD/24hr/C0V77.html"
  res = requests.get(URL)
  soup = BeautifulSoup(res.text, 'html.parser')
  divs = soup.find_all("td", {"headers": "hum"})
  humidity = divs[0].string

  divs = soup.find_all("span", {"class": "tem-C is-active"})
  temperature = divs[0].string

  print(humidity, temperature)
  ip = 'https://plantmonitor.mooo.com'
  try:
    check = float(temperature)
    # Post data
    data = {
            'raspberry_secret_key': secret_data['raspberry_secret_key'],
            'temperature_string': temperature,
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(ip+'/temperature', data=json.dumps(data), headers=headers)
    
    # log message
    # Post data
    data = {
            'raspberry_secret_key': secret_data['raspberry_secret_key'],
            'title': "TEMP",
            'msg': "[Crawker] TEMP data updated",
            'type': "LOG"
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(ip+'/writeLogMessage', data=json.dumps(data), headers=headers)
    
  except ValueError:
    # Post data
    data = {
            'raspberry_secret_key': secret_data['raspberry_secret_key'],
            'title': "TEMP",
            'msg': "[Crawker] TEMP data failed",
            'type': "WARNING"
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(ip+'/writeLogMessage', data=json.dumps(data), headers=headers)
  
  try:
    check = float(humidity)
    # Post data
    data = {
            'raspberry_secret_key': secret_data['raspberry_secret_key'],
            'humidity_string': humidity,
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(ip+'/humidity', data=json.dumps(data), headers=headers)
    
    # log message
    # Post data
    data = {
            'raspberry_secret_key': secret_data['raspberry_secret_key'],
            'title': "HUMID",
            'msg': "[Crawker] HUMID data updated",
            'type': "LOG"
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(ip+'/writeLogMessage', data=json.dumps(data), headers=headers)
    
  except ValueError:
    # Post data
    data = {
            'raspberry_secret_key': secret_data['raspberry_secret_key'],
            'title': "HUMID",
            'msg': "[Crawker] HUMID data failed",
            'type': "WARNING"
    }
    headers = {'content-type': 'application/json'}
    r = requests.post(ip+'/writeLogMessage', data=json.dumps(data), headers=headers)
  break
