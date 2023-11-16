# -*- coding: utf-8 -*- 
# 스크렙

import time
import sys
import json
import io
import os
import requests
import traceback
import random

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

#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')



MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)

SiteUrl = MConfig['SiteUrl']
SetAgent = MConfig['SetAgent']

ChromeVer = "114"
if SetAgent != "" :
	sys.path.append(os.path.dirname("/home/ntosmini/public_html/_agent.py"))
	import _agent

	if SetAgent = "mobile" :
		Agent = _agent.get_mobile_agent()
	elif SetAgent = "pc" :
		Agent = _agent.get_pc_agent()
	else :
		Agent = ""

def chromeWebdriver():
	chrome_service = ChromeService(ChromeDriverManager().install())
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
	if Agent != "" :
		chrome_options.add_argument('--user-agent=' + Agent)
	if ChromeVer :
		driver = uc.Chrome(service=chrome_service, options=chrome_options, version_main=ChromeVer)
	else :
		driver = uc.Chrome(service=chrome_service, options=chrome_options, use_subprocess=True)
	return driver

driver = chromeWebdriver()
driver.get(SiteUrl)
driver.implicitly_wait(10)

PageHtml = driver.page_source
NowUrl = driver.current_url
print(str(NowUrl))
print("\n\n")
print(str(PageHtml))

driver.quit()