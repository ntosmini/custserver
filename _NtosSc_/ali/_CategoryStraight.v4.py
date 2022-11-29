# -*- coding: utf-8 -*- 
# 카테고리 멀티-v4

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
import requests

#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


try :
	os.system("killall -o 3m chrome")
	os.system("killall -o 3m chromedriver")
except :
	pass

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#pip3 install webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

CslId_SiteUrl = []


MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)


NtosServer = MConfig['NtosServer']
CslId_SiteUrl = MConfig['CslId_SiteUrl']
Agent = MConfig['Agent']
NotsKey = MConfig['NotsKey']
CustId = MConfig['CustId']
ScrapServer = MConfig['ScrapServer']
Scroll = MConfig['Scroll']
TimeChk = MConfig['TimeChk']

if TimeChk == "Y" :
	start_time = time.time()

executable_path = ChromeDriverManager().install()

def chromeWebdriver():
	chrome_service = ChromeService(executable_path)
	chrome_options = Options()
	chrome_options.add_experimental_option('detach', True)
	chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--blink-settings=imagesEnabled=false')
	chrome_options.add_argument('window-size=1920,1080')
	chrome_options.add_argument('--disable-dev-shm-usage')
	chrome_options.add_argument('--disable-blink-features=AutomationControlled')
	chrome_options.add_argument('--disable-infobars')
	chrome_options.page_load_strategy = 'normal'
	if Agent == "" :
		chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36")
	else :
		chrome_options.add_argument("user-agent="+ Agent)


	driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

	return driver


driver = chromeWebdriver()

wait = WebDriverWait(driver, 10, 1)

driver.get("https://aliexpress.com")
wait.until( 	EC.presence_of_element_located((By.CLASS_NAME, "logo-base")) )

for val in CslId_SiteUrl :
	(CslId, SiteUrl, log_id) = val.split("|@|")
	PageHtml = ""
	NowUrl = ""

	try :
		driver.get(SiteUrl)

		wait.until( 	EC.presence_of_element_located((By.CLASS_NAME, "logo-base")) )
		#driver.execute_script("window.stop();")

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


		PageHtml = driver.page_source
		NowUrl = driver.current_url
	except :
		pass

	data = {'NtosServer':str(NtosServer), 'NotsKey':NotsKey, 'CustId':CustId, 'ScrapServer':ScrapServer, 'CslId':CslId, 'log_id': log_id, 'NowUrl':str(NowUrl), 'PageHtml':str(PageHtml) }
	headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

	try :
		Result__ = requests.post(NtosServer, data=json.dumps(data), headers=headers)
		Result_ = Result__.text
	except :
		Result_ = "requests_error"
	print(Result_)

driver.quit()
if TimeChk == "Y" :
	print("\n\n--- %s seconds ---" % (time.time() - start_time))
