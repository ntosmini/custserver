# -*- coding: utf-8 -*- 
# 카테고리 파일-v4

import sys
import io
import random
import time
import traceback

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#pip3 install webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import undetected_chromedriver as uc
uc.TARGET_VERSION = 103



#from fake_useragent import UserAgent


#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

ErrHtml = ''
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

try :
	driver = chromeWebdriver()
except :
	ErrHtml = traceback.format_exc()

print(str(ErrHtml))
#driver.delete_all_cookies()

driver.get( 'http://ntos.co.kr' )


PageHtml = driver.page_source
NowUrl = driver.current_url
print(PageHtml)
print(NowUrl)
time.sleep(3)
