# -*- coding: utf-8 -*- 
# 카테고리 멀티-v3

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

#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')



try :
	os.system("killall -o 3m chrome")
	os.system("killall -o 3m chromedriver")
except :
	pass

from selenium import webdriver
from selenium.webdriver.common.alert import Alert

process_list = []


MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)


NtosServer = MConfig['NtosServer']
process_list = MConfig['SclId_SiteUrl']
Agent = MConfig['Agent']
CodeLen = int(MConfig['CodeLen'])
NotsKey = MConfig['NotsKey']
CustId = MConfig['CustId']
Scroll = MConfig['Scroll']
Refresh = MConfig['Refresh']
Referer = MConfig['Referer']
TimeChk = MConfig['TimeChk']

if TimeChk == "Y" :
	start_time = time.time()
	
def multiSelenium(process):
	
	(SclId, SiteUrl, log_id) = process.split("|@|")
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("-disable-notifications")
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--disable-dev-shm-usage')
	chrome_options.add_argument("--blink-settings=imagesEnabled=false")
	chrome_options.add_argument("--window-size=1920x1080")
	if Agent == "" :
		chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36")
	else :
		chrome_options.add_argument("user-agent="+ Agent)


	driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=chrome_options)

	PageHtml = ""
	NowUrl = ""
	try :
		driver.get(SiteUrl)
		driver.implicitly_wait(10)
		
		if Referer :
			driver.get(Referer)
			driver.implicitly_wait(10)
			
		if Refresh == "Y" :
			driver.refresh()
			driver.implicitly_wait(10)

		if Scroll == "Y" :
			SCROLL_PAUSE_SEC = 0.5
			# 스크롤 높이 가져옴
			last_height = driver.execute_script("return document.body.scrollHeight")

			while True:
				# 끝까지 스크롤 다운
				driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

				# 1초 대기
				time.sleep(SCROLL_PAUSE_SEC)

				# 스크롤 다운 후 스크롤 높이 다시 가져옴
				new_height = driver.execute_script("return document.body.scrollHeight")
				if new_height == last_height:
					break
				last_height = new_height


		time.sleep(random.randint(1, 2))
		PageHtml = driver.page_source
		NowUrl = driver.current_url
	except :
		pass



	data = {'NtosServer':str(NtosServer), 'NotsKey':NotsKey, 'CustId':CustId, 'SclId':SclId, 'log_id': log_id, 'NowUrl':str(NowUrl), 'PageHtml':str(PageHtml) }
	headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

	Result_ = ""
	try :
		Result__ = requests.post(NtosServer, data=json.dumps(data), headers=headers)
		Result_ = Result__.text
	except :
		Result_ = "error"

	print(Result_)
	driver.quit()


if __name__ == '__main__':
	pool = multiprocessing.Pool(processes=len(process_list))
	pool.map(multiSelenium, process_list)
	if TimeChk == "Y" :
		print("\n\n--- %s seconds ---" % (time.time() - start_time))
	pool.close()
	pool.join()
	sys.exit()

