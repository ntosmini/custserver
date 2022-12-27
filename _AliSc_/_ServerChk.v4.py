# -*- coding: utf-8 -*- 
# 서버체크 - v3

import time
import sys
#pip install beautifulsoup4     <=> pip install bs4
import json
import io
import requests

#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#pip3 install webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)


CustId = MConfig['CustId']
SiteUrl = MConfig['SiteUrl']
Server = MConfig['Server']
ReturnUrl = MConfig['ReturnUrl']
Sid = MConfig['Sid']

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
	driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
	return driver


driver = chromeWebdriver()

try :
	driver.get(SiteUrl)
	driver.implicitly_wait(10)

	PageHtml = driver.page_source
	NowUrl = driver.current_url
except :
	PageHtml = ''
	NowUrl = ''

data = {'CustId':str(CustId), 'Server':str(Server), 'Sid':str(Sid), 'NowUrl':str(NowUrl), 'PageHtml':str(PageHtml) }
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

requests.post(ReturnUrl, data=json.dumps(data), headers=headers)

driver.quit()
