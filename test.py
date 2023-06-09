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


def chromeWebdriver():
	chrome_service = ChromeService(ChromeDriverManager().install())
	chrome_options = uc.ChromeOptions()
	#chrome_options.add_argument('--headless')
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


driver.get("https://www.dhgate.com")
getcookies = driver.get_cookies()
driver.delete_all_cookies()

NowUrl = driver.current_url


print(NowUrl+"<br><br>")
for cookie in getcookies :
	arr = {}
	if cookie['name'] == "b2b_ship_country" :
		cookie['value'] = "KR"
	if cookie['name'] == "b2b_ip_country" :
		cookie['value'] = "US"

	for val in cookie.keys() :
		arr[val] = cookie[val]
	driver.add_cookie(arr)

	print(cookie)
	print("<br><br>")



driver.get("https://kr.dhgate.com/product/fashion-classic-4-four-leaf-clover-necklaces/741060105.html?dspm=pckr.hp.ymljfy.jfy-2.HwwaCqwyg964Smn0w28w&resource_id=741060105&scm_id=rec.yml..._pc_recm-1to2_pc_nebula_related_pc_recm_fm-jfy-filter_2512_null_greenScreenFlag_6.782263339506557.")
time.sleep(10)
PageHtml = driver.page_source
print("<br><br>"+PageHtml)
