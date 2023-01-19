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
import random

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
Scroll = MConfig['Scroll']

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
NowUrl = ""
try :
	driver = chromeWebdriver()
	driver.get(SiteUrl)
	driver.implicitly_wait(10)

	if Scroll == "Y" :
		SCROLL_PAUSE_SEC = 0.5
		# 스크롤 높이 가져옴
		last_height = driver.execute_script("return document.body.scrollHeight")

		while True:
			# 끝까지 스크롤 다운
			driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

			# SCROLL_PAUSE_SEC 초 대기
			time.sleep(SCROLL_PAUSE_SEC)

			# 스크롤 다운 후 스크롤 높이 다시 가져옴
			new_height = driver.execute_script("return document.body.scrollHeight")
			if new_height == last_height:
				break
			last_height = new_height

	time.sleep(random.randint(1, 3))
	NowUrl = driver.current_url

	page_html = driver.page_source
	print("<ntosoriginurl>"+str(SiteUrl)+"</ntosoriginurl>")
	print("<ntosnowurl>"+str(NowUrl)+"</ntosnowurl>")
	print(page_html)
	driver.close()
	driver.quit()
except :
	err = traceback.format_exc()
	print(str(err))
	driver.close()
	driver.quit()

