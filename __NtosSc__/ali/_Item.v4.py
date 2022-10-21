# -*- coding: utf-8 -*- 
#상품 멀티-v4

import time
import sys
import json
import io
import os
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


MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)

NtosServer = MConfig['NtosServer']
SlId_SiteUrl = MConfig['SlId_SiteUrl']
NotsKey = MConfig['NotsKey']
CustId = MConfig['CustId']
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
	chrome_options.add_argument('--disable-gpu')
	chrome_options.add_argument("--blink-settings=imagesEnabled=false")
	chrome_options.add_argument("window-size=1920,1080")
	
	driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

	return driver


(SlId, SiteUrl, log_id) = SlId_SiteUrl.split("|@|")

driver = chromeWebdriver()
PageHtml = ""
NowUrl = ""
try :
	driver.get(SiteUrl)
	driver.implicitly_wait(5)
	PageHtml = driver.page_source
	NowUrl = driver.current_url
except :
	pass

data = {'NtosServer':str(NtosServer), 'NotsKey':NotsKey, 'CustId':CustId, 'SlId':SlId, 'PageHtml':str(PageHtml), 'log_id': log_id, 'NowUrl':str(NowUrl) }
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

Result_ = ""
try :
	Result__ = requests.post(NtosServer, data=json.dumps(data), headers=headers)
	Result_ = Result__.text
except :
	Result_ = "error"

print(Result_)
driver.quit()

if TimeChk == "Y" :
	print("\n\n--- %s seconds ---" % (time.time() - start_time))