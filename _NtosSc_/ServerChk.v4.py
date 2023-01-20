# -*- coding: utf-8 -*- 
# 서버체크 v4
import sys
import json
import traceback

MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)
SiteUrl = MConfig['SiteUrl']

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#pip3 install webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

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
	driver.close()
	driver.quit()
  print(PageHtml)
except :
	err = traceback.format_exc()
	print(str(err))
	driver.close()
	driver.quit()
