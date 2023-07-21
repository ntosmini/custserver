# -*- coding: utf-8 -*- 
# 서버체크 v4
import sys
import json
import requests
import traceback

MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)

CustId = MConfig['SiteUrl']
SId = MConfig['SiteUrl']
NtosServer = MConfig['SiteUrl']
SiteUrl = MConfig['SiteUrl']
ChromeVer = MConfig['ChromeVer']

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#pip3 install webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import undetected_chromedriver as uc

def chromeWebdriver():
	chrome_service = ChromeService(executable_path = ChromeDriverManager().install())
	chrome_options = uc.ChromeOptions()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--blink-settings=imagesEnabled=false')
	chrome_options.add_argument('--start-maximized')
	chrome_options.add_argument('--disable-dev-shm-usage')
	chrome_options.add_argument('--disable-blink-features=AutomationControlled')
	chrome_options.add_argument('--disable-infobars')
	chrome_options.add_argument('--ignore-certificate-errors')
	chrome_options.add_argument('--ignore-ssl-errors=yes')
	chrome_options.add_argument('--disable-gpu')
	if ChromeVer :
		driver = uc.Chrome(service=chrome_service, options=chrome_options, version_main=ChromeVer)
	else :
		driver = uc.Chrome(service=chrome_service, options=chrome_options, use_subprocess=True)
	return driver


driver = chromeWebdriver()
PageHtml = ''
try :
	driver.get(SiteUrl)
	driver.implicitly_wait(10)
	PageHtml = driver.page_source
	driver.close()
	driver.quit()
except :
	PageHtml = 'ntosseleniumfalse'
CustId = MConfig['SiteUrl']
SId = MConfig['SiteUrl']
NtosServer = MConfig['SiteUrl']
SiteUrl = MConfig['SiteUrl']

data = {'CustId':str(CustId), 'SId':str(SId), 'PageHtml':str(PageHtml) }
requests.post(NtosServer, data=json.dumps(data))
