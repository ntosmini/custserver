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
from selenium.webdriver.common.alert import Alert


MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)


CustId = MConfig['CustId']
SiteUrl = MConfig['SiteUrl']
NtosServer = MConfig['NtosServer']
Sid = MConfig['Sid']


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("-disable-notifications")
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--blink-settings=imagesEnabled=false")
chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=chrome_options)

try :
	driver.get(SiteUrl)
	driver.implicitly_wait(10)

	PageHtml = driver.page_source
	NowUrl = driver.current_url
except :
	PageHtml = ''
	NowUrl = ''

data = {'CustId':CustId, 'Sid':Sid, 'NowUrl':str(NowUrl), 'PageHtml':str(PageHtml) }
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

requests.post(NtosServer, data=json.dumps(data), headers=headers)

driver.quit()
