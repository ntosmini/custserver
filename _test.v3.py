# -*- coding: utf-8 -*- 
# 테스트

import time
import sys
import codecs
import random
#pip install beautifulsoup4     <=> pip install bs4
import threading
import json
import re
import io
import os
import multiprocessing
import requests
import traceback

#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)

SiteUrl = MConfig['SiteUrl']

from selenium import webdriver
from selenium.webdriver.common.alert import Alert

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("-disable-notifications")
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=chrome_options)

try :
	driver.get(SiteUrl)
	driver.implicitly_wait(10)
	page_html = driver.page_source
	print(page_html)
	driver.close()
	driver.quit()
except :
	err = traceback.format_exc()
	print(str(err))
	driver.close()
	driver.quit()
