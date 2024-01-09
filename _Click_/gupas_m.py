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


MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)


Type = MConfig['Type']
SiteUrl = MConfig['SiteUrl']
Search1 = MConfig['Search1']
SearchChk = MConfig['SearchChk']


if Type == "server" :
	sys.path.append(os.path.dirname("/home/ntosmini/public_html/_agent.py"))
else :
	sys.path.append(os.path.dirname("C:/_Click_/_agent.py"))

import _agent

#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

def ScrollDown(sec, sc_type='') :
	SCROLL_PAUSE_SEC = sec
	# 스크롤 높이 가져옴
	last_height = driver.execute_script("return document.body.scrollHeight")

	driver.execute_script("window.scrollTo(0, 0);")
	time.sleep(random.randint(1, 2))

	if sc_type == "num" :

		num = random.randint(5, 10)
		n_sc = last_height / num
		for i in range(num) :
			driver.execute_script("window.scrollTo(0, "+str(n_sc)+");")
			time.sleep(sec)
			new_height = driver.execute_script("return document.body.scrollHeight")
			if new_height == n_sc:
				break
			last_height = new_height
			n_sc = n_sc + n_sc
	else :
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

def chromeWebdriver():
	agent = _agent.get_mobile_agent()
	if Type == "server" :
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
	else :
		chrome_options = Options()
		driver = webdriver.Chrome(options=chrome_options)
	return driver


driver = chromeWebdriver()
driver.delete_all_cookies()

time.sleep(random.randint(1, 2))
driver.get(SiteUrl)
driver.implicitly_wait(10)
time.sleep(random.randint(2, 5))
#driver.maximize_window()




time.sleep(random.randint(2, 5))


#검색시작 >>>>>>>>>>>>>>>>>>>>
driver.find_element(By.XPATH, '//*[@id="MM_SEARCH_FAKE"]').click()

time.sleep(random.randint(1, 2))
SearchForm = driver.find_element(By.XPATH, '//*[@id="query"]')
SearchForm.click()

for val in list(Search1) :
	SearchForm.send_keys(str(val))
	time.sleep(random.uniform(0.1, 0.5))

SearchForm.send_keys(Keys.ENTER)
time.sleep(random.randint(2, 7))


MatchChk = "n"

try :

	Search1_tags = driver.find_elements(By.TAG_NAME, "a")

	for Val in Search1_tags :
		if Val.text == SearchChk :
			Val.click()
			MatchChk = "y"
			break


	if MatchChk == "n" :
		g_elements = driver.find_elements(By.XPATH, '//*[@class="group_more"]')
		g_elements[0].click()
		time.sleep(random.randint(5, 10))

		Search1_tags_ = driver.find_elements(By.TAG_NAME, "a")

		for Val2 in Search1_tags_ :
			if Val2.text == SearchChk :
				Val2.click()
				MatchChk = "y"
				break

		time.sleep(random.randint(10, 15))

	if MatchChk == "y" :
		driver.set_window_size(768, 1366)
		time.sleep(random.randint(5, 9))
		time.sleep(random.randint(5, 10))
		ScrollDown(random.uniform(0.5, 1), 'num')
		time.sleep(random.randint(15, 22))


		driver.find_element(By.CLASS_NAME, "xi-bars").click()
		time.sleep(random.randint(3, 7))
		a_elements = driver.find_elements(By.CLASS_NAME, 'css-1q0anj3')
		a_elements[random.randint(0, len(a_elements)-1)].click()
		time.sleep(random.randint(3, 7))
		ScrollDown(random.uniform(0.5, 1), 'num')

		time.sleep(random.randint(33, 55))

		driver.back()

		time.sleep(random.randint(3, 7))
		try :
			driver.refresh()
			time.sleep(random.randint(1, 5))
		except :
			pass
		ScrollDown(random.uniform(0.5, 1), 'num')
		time.sleep(random.randint(40, 65))


		print("SUCCESS")

except :
	print("FALSE")
	print(str(traceback.format_exc()))

# 종료
driver.quit()
