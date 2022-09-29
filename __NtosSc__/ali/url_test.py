# -*- coding: utf-8 -*- 
# 알리 카테고리 멀티

import time
import sys
import codecs
import random
#pip install beautifulsoup4     <=> pip install bs4
import threading
import json
import re
import io
import os
import multiprocessing
import requests

#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


from selenium import webdriver
from selenium.webdriver.common.alert import Alert

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("-disable-notifications")
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=chrome_options)

MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)


SiteUrl = MConfig['SiteUrl']
print("접근 Url : "+ str(SiteUrl))
try :
	driver.get(SiteUrl)
	driver.implicitly_wait(10)
	driver.refresh()
	driver.implicitly_wait(5)
	time.sleep(random.randint(3, 5))
	nowurl = driver.current_url

	page_html = driver.page_source
	print("<br>최종 Url : "+str(nowurl))
	print("<br>--------------------------------------<br>")
	print("--------------------------------------<br><br>")
	print(page_html)
	driver.close()
	driver.quit()
except :
	print("except")
	driver.close()
	driver.quit()
