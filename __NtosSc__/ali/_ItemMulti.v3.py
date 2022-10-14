# -*- coding: utf-8 -*- 
#상품 멀티-v3

import time
import sys
import json
import io
import os
import multiprocessing
import requests
from selenium import webdriver

#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

try :
	os.system("killall -o 3m chrome")
	os.system("killall -o 3m chromedriver")
except :
	pass

process_list = []

MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)

NtosServer = MConfig['NtosServer']
process_list = MConfig['SlId_SiteUrl']
NotsKey = MConfig['NotsKey']
CustId = MConfig['CustId']
TimeChk = MConfig['TimeChk']

if TimeChk == "Y" :
	start_time = time.time()

def multiSelenium(process):
	(SlId, SiteUrl, log_id) = process.split("|@|")
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("-disable-notifications")
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--disable-dev-shm-usage')
	chrome_options.add_argument("--window-size=1920x1080")
	chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36")
	driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=chrome_options)

	PageHtml = ""
	NowUrl = ""
	try :
		driver.get(SiteUrl)
		driver.implicitly_wait(5)
		PageHtml = driver.page_source
		NowUrl = driver.current_url
	except :
		pass

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

if __name__ == '__main__':
	pool = multiprocessing.Pool(processes=len(process_list))
	pool.map(multiSelenium, process_list)
	if TimeChk == "Y" :
		print("\n\n--- %s seconds ---" % (time.time() - start_time))
	pool.close()
	pool.join()
	sys.exit()
