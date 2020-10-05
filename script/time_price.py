# http://khfv.com.tw/pagepub/AppContent.aspx?GP=GP04.01
import requests
from bs4 import BeautifulSoup
import time
import re
import os
import urllib
import json
import io
from datetime import datetime, timedelta

while True:

  URL = "http://khfv.com.tw/pagepub/AppContent.aspx?GP=GP04.01"
  res = requests.get(URL)
  soup = BeautifulSoup(res.text, 'html.parser')
  divs = soup.find_all("table", {"id": "WR1_1_WG1"})
  divs = divs[0].find_all("tr", {"class": "CSS_AWG_RowB"})
  for div in divs:
      date_string = div.find_all("td", {"align": "left","valign": "middle"})[0].string.replace('/', '_') #[0] : date
      product_string = div.find_all("td", {"align": "left","valign": "middle"})[1].string #[1] : product code
      average_price_string = div.find_all("td", {"align":"right","valign": "middle"})[3].string #[3] : average_price

      if(product_string=="LF2"):
          today = datetime.today()
          if(date_string == today.strftime('%Y_%m_%d')):
              print(date_string)
              print(product_string)
              print(average_price_string)
      
          # Post data
          product_name = 'water_spinach'
          ip = 'http://10.1.1.16:8000'
          data = '/timePrice/'+ average_price_string +'/date/'+ date_string + '/product/' + product_name
          print(data)
          try:
              r = requests.get(ip+data)
          except:
              print("failed to connect to server")
              break
  break

