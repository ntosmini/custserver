# -*- coding: utf-8 -*- 

import time
import sys
import json
import io
import os
import requests
import traceback

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains

#pip3 install webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import undetected_chromedriver as uc

#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
PageHtml = ''
try :
  subprocess.Popen(f'google-chrome --remote-debugging-port=9222  --user-data-dir=data_dir'.split()) 
  
  option = Options()
  option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
  chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
  
  try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver', options=option)
  except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver', options=option)
    print(str(traceback.format_exc()))
  
  driver.get("http://ntos.co.kr")
  driver.implicitly_wait(10)
  PageHtml = driver.page_source
except :
  print(str(traceback.format_exc()))
print(PageHtml)
