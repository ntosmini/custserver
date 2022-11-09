# -*- coding: utf-8 -*- 
#상품 스트레이트-v3

import time
import sys
import json
import io
import os
import re
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

try :
	os.system("killall -o 3m chrome")
	os.system("killall -o 3m chromedriver")
except :
	pass

IslId_SiteUrl = []


MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)

NtosServer = MConfig['NtosServer']
IslId_SiteUrl = MConfig['IslId_SiteUrl']
NotsKey = MConfig['NotsKey']
CustId = MConfig['CustId']
TimeChk = MConfig['TimeChk']
LogChkUrl = MConfig['LogChkUrl']
chk_idx = MConfig['chk_idx']


if TimeChk == "Y" :
	start_time = time.time()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("-disable-notifications")
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36")
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument('--disable-infobars')
chrome_options.page_load_strategy = 'normal'

driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=chrome_options)

wait = WebDriverWait(driver, 10, 1)

for val in IslId_SiteUrl :
	(IslId, SiteUrl, log_id) = val.split("|@|")

	if LogChkUrl :
		try :
			requests.post(LogChkUrl, data=json.dumps({'CustId':CustId, 'log_id':log_id, 'Step':'1' }), headers={'Content-Type': 'application/json', 'Accept': 'application/json'})
		except :
			pass

	PageHtml = ""
	NowUrl = ""
	


	try :
		driver.get(SiteUrl)
		wait.until( EC.presence_of_element_located((By.CLASS_NAME, "logo-base")) )
		#driver.execute_script("window.stop();")

		PageHtml = driver.page_source
		NowUrl = driver.current_url
		

		if LogChkUrl :
			try :
				requests.post(LogChkUrl, data=json.dumps({'CustId':CustId, 'log_id':log_id, 'Step':'2' }), headers={'Content-Type': 'application/json', 'Accept': 'application/json'})
			except :
				pass
		
	except :
		pass

	data = {'NtosServer':str(NtosServer), 'NotsKey':NotsKey, 'CustId':CustId, 'IslId':IslId, 'PageHtml':str(PageHtml), 'log_id': log_id, 'chk_idx': chk_idx, 'NowUrl':str(NowUrl) }
	headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

	Result_ = ""
	try :
		Result__ = requests.post(NtosServer, data=json.dumps(data), headers=headers)
		Result_ = Result__.text
		
		if LogChkUrl :
			try :
				requests.post(LogChkUrl, data=json.dumps({'CustId':CustId, 'log_id':log_id, 'Step':'3' }), headers={'Content-Type': 'application/json', 'Accept': 'application/json'})
			except :
				pass
		
	except :
		Result_ = "error"

	print(Result_)
	

driver.quit()
if TimeChk == "Y" :
	print("\n\n--- %s seconds ---" % (time.time() - start_time))
