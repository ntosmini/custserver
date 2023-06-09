# -*- coding: utf-8 -*- 
# 쿠키

import time
import sys
import json
import io
import os
import requests
import traceback

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

import undetected_chromedriver as uc

from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse, unquote

try :
	ChromeVer = sys.argv[1]

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
		chrome_options.page_load_strategy = 'normal'
		if ChromeVer == "" :
			driver = uc.Chrome(service=chrome_service, options=chrome_options, use_subprocess=True)
		   else :
			driver = uc.Chrome(service=chrome_service, options=chrome_options, version_main=ChromeVer)
		return driver

	driver = chromeWebdriver()


	driver.get("http://ntos.co.kr")
	getcookies = driver.get_cookies()
	driver.delete_all_cookies()

	NowUrl = driver.current_url
	PageHtml = driver.page_source

	print(NowUrl+"<br><br>")
	print(PageHtml+"<br><br>")
except :
	err = traceback.format_exc()
	return str(err)
