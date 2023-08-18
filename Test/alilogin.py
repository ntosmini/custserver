# -*- coding: utf-8 -*- 
#알리 상품 모바일 uc
import time
import sys
import json
import io
import os
import random
import requests
import traceback
import re

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#pip3 install webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains

import undetected_chromedriver as uc
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse, unquote


from selenium.webdriver.common.keys import Keys
#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

ChromeVer = "114"
sys.path.append(os.path.dirname("/home/ntosmini/public_html/_agent.py"))
import _agent
pc_agent = _agent.get_mobile_agent()

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
	chrome_options.add_argument('--user-agent=' + pc_agent)
	if ChromeVer :
		driver = uc.Chrome(service=chrome_service, options=chrome_options, version_main=ChromeVer)
	else :
		driver = uc.Chrome(service=chrome_service, options=chrome_options, use_subprocess=True)
	return driver
try :
	driver = chromeWebdriver()

	driver.get("https://login.aliexpress.com/?return_url=https:%3A%2F%2Fm.aliexpress.us")

	driver.implicitly_wait(10)
	iframe = driver.find_elements(By.TAG_NAME, "iframe")
	for iframeVal in iframe :
		driver.switch_to.frame(iframeVal)
		try :
			slider2 = driver.find_element(By.ID, "nc_1_n1z")
			if slider2 :
				time.sleep(random.uniform(0.5, 2))
				#slider2.click()
				action.move_to_element(slider2)
				action.click_and_hold(slider2)
				action.move_by_offset(random.uniform(300, 350), random.randint(-1, 1))
				action.release()
				action.perform()
				driver.switch_to.default_content()
				driver.implicitly_wait(10)
				PageHtml = driver.page_source
		except :
			pass
		driver.switch_to.default_content()
	time.sleep(random.uniform(1, 3))

	try :
		driver.find_element(By.XPATH, '//*[@class="pop-close-btn"]').click()
		time.sleep(random.uniform(1, 3))
	except :
		print("pass")
		pass

	PageHtml = driver.page_source

	time.sleep(random.uniform(1, 3))
	#driver.find_element(By.XPATH, '//*[@class="comet-icon comet-icon-account _3L9my"]').click()
	
	try :
		time.sleep(random.uniform(1, 3))
		driver.find_element(By.XPATH, '//*[@class="scene-login-icon-more"]').click()
	except :
		pass

	try :
		time.sleep(random.uniform(1, 3))
		driver.find_element(By.XPATH, '//*[@class="cosmos-tabs-nav-item"]').click()
	except :
		pass




	time.sleep(random.uniform(1, 3))
	id_input = driver.find_element(By.XPATH, '//*[@id="fm-login-id"]')
	user_id = "ntosmini@gmail.com"
	for val in list(user_id) :
		id_input.send_keys(str(val))
		time.sleep(random.uniform(0.01, 0.5))

	time.sleep(2)

	pw_input = driver.find_element(By.XPATH, '//*[@id="fm-login-password"]')
	user_pw = "wjdalsl!!22"
	for val in list(user_pw) :
		pw_input.send_keys(str(val))
		time.sleep(random.uniform(0.01, 0.5))
	time.sleep(2)

	driver.find_element(By.CLASS_NAME, 'login-submit').click()




	time.sleep(random.uniform(1, 3))
	driver.get("https://login.aliexpress.com/?return_url=https:%3A%2F%2Fm.aliexpress.us")
	driver.implicitly_wait(10)
	PageHtml11 = driver.page_source
	NowUrl = driver.current_url
	print(str(NowUrl)+"<br><br>"+str(PageHtml11))

except :
	print(str(traceback.format_exc()))
driver.quit()
