# -*- coding: utf-8 -*- 
# 알리 카테고리 멀티

import time
import sys
import json
import io
import os
import multiprocessing
import requests

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

#pip3 install webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

try :
	os.system("killall -o 3m chrome")
	os.system("killall -o 3m chromedriver")
except :
	pass



start_time = time.time()

def chromeWebdriver():
	#chrome_service = ChromeService(executable_path=ChromeDriverManager().install())
	chrome_options = Options()
	chrome_options.add_experimental_option('detach', True)
	chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument("window-size=1920,1080")
	driver = webdriver.Chrome("/usr/bin/chromedriver", options=chrome_options)

	return driver

driver = chromeWebdriver()
SiteUrl = "http://ntos.co.kr"
driver.get(SiteUrl)
driver.implicitly_wait(5)
PageHtml = driver.page_source

print(PageHtml)
driver.close()
driver.quit()
