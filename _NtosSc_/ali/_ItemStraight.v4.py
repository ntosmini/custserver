# -*- coding: utf-8 -*- 
#상품 스트레이트-v4

import time
import sys
import json
import io
import os
import requests

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

IslId_SiteUrl = []


MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)

NtosServer = MConfig['NtosServer']
IslId_SiteUrl = MConfig['IslId_SiteUrl']
NotsKey = MConfig['NotsKey']
CustId = MConfig['CustId']
TimeChk = MConfig['TimeChk']
LogChkUrl = MConfig['LogChkUrl']
WaitChk = MConfig['WaitChk']
chk_idx = MConfig['chk_idx']

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
	if WaitChk == "Y" :
		chrome_options.page_load_strategy = 'normal'

	driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

	return driver

driver = chromeWebdriver()

if WaitChk == "Y" :
	# 기본적으로 10초를 기다리고 다음 스크립트 실행
	wait = WebDriverWait(driver, 10, 2)

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
		if WaitChk == "Y" :
			# logo-base 클래스가 나타날때까지 기다린다.
			wait.until(
				EC.presence_of_element_located((By.CLASS_NAME, "logo-base"))
			)
			# javascript 실행을 중지시킨다.
			driver.execute_script("window.stop();")
		else :
			driver.implicitly_wait(10)
		
		PageHtml = driver.page_source
		NowUrl = driver.current_url
		

		if LogChkUrl :
			try :
				requests.post(LogChkUrl, data=json.dumps({'CustId':CustId, 'log_id':log_id, 'Step':'2' }), headers={'Content-Type': 'application/json', 'Accept': 'application/json'})
			except :
				pass
		
	except :
		print("except")
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
