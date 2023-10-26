# -*- coding: utf-8 -*- 

import time
import sys
import io
import random
import os
import datetime
import re
import traceback
import json
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


#pip3 install webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# 파일로 접근
import undetected_chromedriver as uc

#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

def ScrollDown(sec) :
	SCROLL_PAUSE_SEC = sec
	# 스크롤 높이 가져옴
	last_height = driver.execute_script("return document.body.scrollHeight")

	while True:
		# 끝까지 스크롤 다운
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

		# 1초 대기
		time.sleep(SCROLL_PAUSE_SEC)

		# 스크롤 다운 후 스크롤 높이 다시 가져옴
		new_height = driver.execute_script("return document.body.scrollHeight")
		if new_height == last_height:
			break
		last_height = new_height
from urllib import parse

Type = sys.argv[1]
StartUrl = sys.argv[2]
Search = sys.argv[3]
SearchChk = sys.argv[4]

StartUrl = parse.unquote(StartUrl)
Search = parse.unquote(Search)
SearchChk = SearchChk.replace(" ", "")
sys.path.append(os.path.dirname("/home/ntosmini/public_html/_agent.py"))

import _agent

agent = _agent.get_mobile_agent()


def chromeWebdriver():
	chrome_service = ChromeService(ChromeDriverManager().install())
	chrome_options = uc.ChromeOptions()
	chrome_options.add_argument('--headless=new')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--blink-settings=imagesEnabled=false')
	chrome_options.add_argument('--window-size=1920,1080')
	chrome_options.add_argument('--disable-dev-shm-usage')
	chrome_options.add_argument('--disable-blink-features=AutomationControlled')
	chrome_options.add_argument('--disable-infobars')
	chrome_options.add_argument('--disable-setuid-sandbox')
	chrome_options.add_argument('--disable-gpu')    
	chrome_options.add_argument('--user-agent=' + agent)
	chrome_options.page_load_strategy = 'normal'
	driver = uc.Chrome(service=chrome_service, options=chrome_options, version_main=113)

	return driver


driver = chromeWebdriver()
driver.delete_all_cookies()
driver.get(StartUrl)
driver.implicitly_wait(10) # 처음에만 셋팅
time.sleep(random.randint(2, 5))

# 검색창 클릭

# 모바일인 경우
driver.find_element(By.XPATH, '//*[@id="MM_SEARCH_FAKE"]').click()

elem = driver.find_element(By.XPATH, '//*[@id="query"]')
time.sleep(random.randint(2, 7))

for val in list(Search) :
	elem.send_keys(str(val))
	time.sleep(random.uniform(0.1, 1))

elem.send_keys(Keys.ENTER)
time.sleep(random.randint(2, 7))

mecotine_chk = 'n'


try :
	e1_elements = driver.find_elements(By.CSS_SELECTOR, "a[href*='https://"+str(SearchChk)+"']")
	if len(e1_elements) == 0:
		pass
	else :
		e1_elements[random.randint(0, len(e1_elements)-1)].click()
		mecotine_chk = "y"
except :
	err = traceback.format_exc()
	print(str(err))
	print("EXCEPT1")



if mecotine_chk == "n" :
	try :
		more = driver.find_elements(By.XPATH, '//*[@class="group_more"]')
		more[0].click()
		time.sleep(random.randint(2, 7))
	except :
		err = traceback.format_exc()
		print(str(err))
		print("EXCEPT4")

	try :
		e2_elements = driver.find_elements(By.CSS_SELECTOR, "a[href*='https://"+str(SearchChk)+"']")
		print(str(len(e2_elements))+"--------------------")
		if len(e2_elements) == 0:
			pass
		else :
			e2_elements[random.randint(0, len(e2_elements)-1)].click()
			mecotine_chk = "y"
	except :
		err = traceback.format_exc()
		print(str(err))
		print("EXCEPT5")


if mecotine_chk == "y" :
	try:

		time.sleep(random.randint(20, 46))

		home_ = driver.find_elements(By.CSS_SELECTOR, "a[href=\"/\"]")
		home_[1].click()

		time.sleep(random.randint(5, 10))

		a_elements = driver.find_elements(By.CSS_SELECTOR, ".main_disp a[href*='shopdetail']")

		a_elements[random.randint(0, len(a_elements)-1)].click()


		time.sleep(random.randint(20, 55))



		print("SUCCESS")

	except:
		err = traceback.format_exc()
		print(str(err))
		print("EXCEPT3")

driver.quit()
