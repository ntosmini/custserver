# -*- coding: utf-8 -*- 


"""

find_element(By.ID, "id")
find_element(By.NAME, "name")
find_element(By.XPATH, "xpath")
find_element(By.LINK_TEXT, "link text")
find_element(By.PARTIAL_LINK_TEXT, "partial link text")
find_element(By.TAG_NAME, "tag name")
find_element(By.CLASS_NAME, "class name")
find_element(By.CSS_SELECTOR, "css selector")

"""


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
Search = MConfig['Search']
SearchChk = MConfig['SearchChk']

if Type == "server" :
	sys.path.append(os.path.dirname("/home/ntosmini/public_html/_agent.py"))
else :
	sys.path.append(os.path.dirname("C:/_Click_/_agent.py"))

import _agent
agent = _agent.get_mobile_agent()

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
		nm_ = num - random.randint(1, 3)
		n_sc = (last_height / num)

		for i in range(nm_) :
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

def TargetClick(Target) :
	global ActionChains
	actions = ActionChains(driver).move_to_element(Target)
	actions.perform()
	time.sleep(random.randint(1, 2))
	Target.click()

def chromeWebdriver():
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
		chrome_options.add_experimental_option('detach', True)
		chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
		#chrome_options.add_argument('--headless')
		chrome_options.add_argument('--no-sandbox')
		chrome_options.add_argument('user-agent=' + agent)

		driver = webdriver.Chrome(options=chrome_options)
	return driver


driver = chromeWebdriver()
driver.delete_all_cookies()

driver.maximize_window()
driver.get(SiteUrl)
driver.implicitly_wait(10)
time.sleep(random.randint(2, 5))


time.sleep(random.randint(2, 5))


#검색시작 >>>>>>>>>>>>>>>>>>>>
driver.find_element(By.XPATH, '//*[@id="MM_SEARCH_FAKE"]').click()


time.sleep(random.randint(1, 2))
SearchForm = driver.find_element(By.XPATH, '//*[@id="query"]')
SearchForm.click()

for val in list(Search) :
	SearchForm.send_keys(str(val))
	time.sleep(random.uniform(0.1, 0.5))

SearchForm.send_keys(Keys.ENTER)
time.sleep(random.randint(2, 7))


MatchChk = "n"

try :

	ScrollDown(random.uniform(0.5, 1), 'num')
	time.sleep(random.randint(1, 2))
	driver.execute_script("window.scrollTo(0, 0);")
	time.sleep(random.randint(1, 2))
	viewmore = driver.find_element(By.CSS_SELECTOR, "a[href*='?where=m_view']")
	TargetClick(viewmore)


	time.sleep(random.randint(1, 3))
	ScrollDown(1, '')
	time.sleep(random.randint(2, 5))

	Search_tags = driver.find_elements(By.TAG_NAME, "a")
	for Val in Search_tags :
		if Val.text == SearchChk and SearchChk :
			TargetClick(Val)
			MatchChk = "y"
			break

	if MatchChk == "y" :
		time.sleep(random.randint(2, 5))
		ScrollDown(random.randint(1, 2), 'num')
		time.sleep(random.randint(20, 35))
		try :
			mecotine = driver.find_element(By.CSS_SELECTOR, ".main_disp a[href*='shopdetail']")
			TargetClick(mecotine)
			time.sleep(random.randint(2, 5))
			driver.switch_to.window(driver.window_handles[-1])
			time.sleep(random.randint(1, 2))
			ScrollDown(random.uniform(0.5, 1), 'num')
			conloop = random.randint(1, 3)
			for l in range(conloop) :
				time.sleep(random.randint(2, 5))
				a_elements = driver.find_elements(By.CSS_SELECTOR, "a[href*='shopdetail']")
				a_emerand = random.randint(0, len(a_elements)-1)
				a_emerand_target = a_elements[a_emerand]
				TargetClick(a_emerand_target)
				
				time.sleep(random.randint(3, 7))
				ScrollDown(random.uniform(0.5, 1), 'num')
				time.sleep(random.randint(10, 22))
				driver.execute_script("window.history.go(-1)")
				time.sleep(random.randint(3, 7))
				ScrollDown(random.uniform(0.5, 1), 'num')
				time.sleep(random.randint(25, 40))
		except :
			print(str(traceback.format_exc()))

	print("SUCCESS")
except :
	print("FALSE")
	print(str(traceback.format_exc()))

# 종료
driver.quit()
