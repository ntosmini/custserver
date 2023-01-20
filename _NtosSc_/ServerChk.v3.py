# -*- coding: utf-8 -*- 
# 서버체크 v3
import sys
import json
import traceback

MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)
SiteUrl = MConfig['SiteUrl']

from selenium import webdriver
from selenium.webdriver.common.alert import Alert

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
	driver.close()
	driver.quit()
	print(PageHtml)
except :
	err = traceback.format_exc()
	print(str(err))
	driver.close()
	driver.quit()
