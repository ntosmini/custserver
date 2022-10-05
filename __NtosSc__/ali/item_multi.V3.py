# -*- coding: utf-8 -*- 
# 알리 카테고리 멀티

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
process_list = MConfig['SlId_SiteUrl']
NotsKey = MConfig['NotsKey']
CustId = MConfig['CustId']

start_time = time.time()




def multiSelenium(process):
	(SlId, SiteUrl, log_id) = process.split("|@|")

	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("-disable-notifications")
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--disable-dev-shm-usage')
	chrome_options.add_argument("--window-size=1920x1080")
	chrome_options.add_argument('--lang=ko_KR')
	chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36")
	driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=chrome_options)

	try :
		driver.get(SiteUrl)
		driver.implicitly_wait(5)
		PageHtml = driver.page_source

		NowUrl = driver.current_url
		"""
		ItemInfoMatched = re.search('\{"actionModule".*\}', PageHtml)
		ItemInfoData = ItemInfoMatched.group()

		ItemInfo = json.loads(ItemInfoData)


		DetailHtml = ''
		DetailUrl = ItemInfo['descriptionModule']['descriptionUrl']

		driver.get(DetailUrl)
		driver.implicitly_wait(5)
		DetailHtml = driver.page_source
		"""

		data = {'NtosServer':str(NtosServer), 'NotsKey':NotsKey, 'CustId':CustId, 'SlId':SlId, 'PageHtml':PageHtml, 'log_id': log_id, 'NowUrl':NowUrl }
		headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

		Result_ = ""
		try :
			Result__ = requests.post(NtosServer, data=json.dumps(data), headers=headers)
			Result_ = Result__.text
		except :
			Result_ = "error"


		print(Result_)

		driver.close()
		driver.quit()

	except :
		data = {'NtosServer':str(NtosServer), 'NotsKey':NotsKey, 'CustId':CustId, 'SlId':SlId, 'PageHtml':'', 'log_id': log_id, 'NowUrl':'' }
		headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
		Result__ = requests.post(NtosServer, data=json.dumps(data), headers=headers)
		print("except")
		driver.close()
		driver.quit()



if __name__ == '__main__':
	pool = multiprocessing.Pool(processes=len(process_list))
	pool.map(multiSelenium, process_list)
	print("\n\n--- %s seconds ---" % (time.time() - start_time))
	pool.close()
	pool.join()
	sys.exit()
