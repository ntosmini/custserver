# -*- coding: utf-8 -*- 
# 쿠키 text

import time
import sys
import json
import io
import os
import requests
import traceback
import re

#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


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

import undetected_chromedriver as uc

from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse, unquote
print("1")

MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)

SiteUrl = MConfig['SiteUrl']
CookiesLang = MConfig['CookiesLang']
print("2")

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
	driver = uc.Chrome(service=chrome_service, options=chrome_options, use_subprocess=True)
	return driver

driver = chromeWebdriver()
print("3")

try :
	if re.search(r'aliexpress', str(SiteUrl)) and CookiesLang :
		if CookiesLang == "en" :
			driver.get('https://aliexpress.us')
		elif CookiesLang == "ko" :
			driver.get('https://ko.aliexpress.com')
		getcookies = driver.get_cookies()
		driver.delete_all_cookies()
		arr = {}
		for cookie in getcookies :
			"""
			if cookie['name'] == "JSESSIONID" :
				cookie['domain'] = 'www.aliexpress.com'
			"""
			parts = ''
			new_url = ''
			qs = {}
			if cookie['name'] == "aep_usuc_f" :
				# site=kor&c_tp=KRW®ion=KR&b_locale=ko_KR
				# site=kor&c_tp=KRW&region=KR&b_locale=ko_KR
				parts = urlparse('https://aliexpress.com?'+cookie['value'])
				qs = dict(parse_qsl(parts.query))
				if CookiesLang == "en" :
					qs['site'] = 'usa'
					qs['c_tp'] = 'USD'
					qs['region'] = 'US'
					qs['b_locale'] = 'en_US'
				elif CookiesLang == "ko" :
					qs['site'] = 'kor'
					qs['c_tp'] = 'KRW'
					qs['region'] = 'KR'
					qs['b_locale'] = 'ko_KR'

				parts = parts._replace(query=urlencode(qs))
				new_url = urlunparse(parts)
				new_url = unquote(new_url.replace('https://aliexpress.com?', ''))
				cookie['value'] = new_url

			if cookie['name'] == "intl_locale" :
				#cookie['value'] = 'ko_KR'
				if CookiesLang == "en" :
					cookie['value'] = "en_US"
				elif CookiesLang == "ko" :
					cookie['value'] = "ko_KR"

			parts = ''
			new_url = ''
			qs = {}
			if cookie['name'] == "xman_us_f" :
				#cookie['value'] = 'x_l=0&x_locale=ko_KR&x_c_chg=1&acs_rt='
				parts = urlparse('https://aliexpress.com?'+cookie['value'])
				qs = dict(parse_qsl(parts.query))
				if CookiesLang == "en" :
					qs['x_locale'] = 'en_US'
				elif CookiesLang == "ko" :
					qs['x_locale'] = 'ko_KR'

				parts = parts._replace(query=urlencode(qs))
				new_url = urlunparse(parts)
				new_url = unquote(new_url.replace('https://aliexpress.com?', ''))
				cookie['value'] = new_url

			for val in cookie.keys() :
				arr[val] = cookie[val]
			print(str(arr)+"<br>")
			driver.add_cookie(arr)
except :
	ErrHtml = traceback.format_exc()
	print(str(ErrHtml))

driver.get(SiteUrl)
PageHtml = driver.page_source
NowUrl = driver.current_url
print(NowUrl+"<br>")
print(PageHtml+"<br>")
