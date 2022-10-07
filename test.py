# -*- coding: utf-8 -*- 
# 테스트

import time
import sys
import json
import io
import os
import multiprocessing
import requests
import traceback

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

#pip3 install webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

executable_path=ChromeDriverManager().install()


try :
	chrome_service = ChromeService(executable_path)
	chrome_options = Options()
	chrome_options.add_experimental_option('detach', True)
	chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument("window-size=1920,1080")
	driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
except Exception:
    err = traceback.format_exc()
    print(str(err))

print(executable_path)
print("")
