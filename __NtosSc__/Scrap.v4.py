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

MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)

SiteUrl = MConfig['SiteUrl']

start_time = time.time()

def chromeWebdriver():
	chrome_service = ChromeService(executable_path=ChromeDriverManager().install())
	chrome_options = Options()
	chrome_options.add_experimental_option('detach', True)
	chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument("--blink-settings=imagesEnabled=false")
	chrome_options.add_argument("window-size=1920,1080")
	driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

	return driver

try :
	driver = chromeWebdriver()
	driver.get(SiteUrl)
	driver.implicitly_wait(10)
	driver.refresh()
	driver.implicitly_wait(5)
	time.sleep(random.randint(1, 3))

	page_html = driver.page_source
	print(page_html)
	driver.close()
	driver.quit()
except :
	print("except")
	driver.close()
	driver.quit()

