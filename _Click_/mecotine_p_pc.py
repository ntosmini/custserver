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
import requests

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

SearchChk1 = MConfig['SearchChk1']
SearchChk2 = MConfig['SearchChk2']
Page = MConfig['Page']


if Type == "server" :
	sys.path.append(os.path.dirname("/home/ntosmini/public_html/_agent.py"))
else :
	sys.path.append(os.path.dirname("C:/_Click_/_agent.py"))

import _agent
agent = _agent.get_pc_agent()

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
	driver.execute_script("window.scrollTo(0, 100);")
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
		chrome_options.add_argument('--no-sandbox')
		chrome_options.add_argument('--disable-dev-shm-usage')
		chrome_options.add_argument('--disable-blink-features=AutomationControlled')
		chrome_options.add_argument('--disable-infobars')
		chrome_options.add_argument('--disable-setuid-sandbox')
		chrome_options.add_argument('--disable-gpu')
		chrome_options.add_argument('--user-agent=' + agent)
		chrome_options.page_load_strategy = 'normal'
		driver = webdriver.Chrome(options=chrome_options)
	return driver


driver = chromeWebdriver()
driver.delete_all_cookies()
driver.maximize_window()
time.sleep(random.randint(1, 2))


driver.get(SiteUrl)
driver.implicitly_wait(10)
time.sleep(random.randint(2, 5))

#검색시작 >>>>>>>>>>>>>>>>>>>>
SearchForm = driver.find_element(By.XPATH, '//*[@id="query"]')
SearchForm.click()

for val in list(Search) :
	SearchForm.send_keys(str(val))
	time.sleep(random.uniform(0.1, 0.5))

SearchForm.send_keys(Keys.ENTER)
time.sleep(random.randint(2, 7))


MatchChk = "n"
NtosUrl = "http://product.ntos.co.kr/_Ntos_/click/mecotine_chk.php"
try :
	ScrollDown(random.uniform(0.5, 1), 'num')
	Search1_tags = driver.find_elements(By.TAG_NAME, "a")

	for Val in Search1_tags :
		if Val.text == SearchChk1 and SearchChk1 :
			TargetClick(Val)
			MatchChk = "y"
			data = {'mode': 'up', 'type':'pc1', 'text':str(Val.text) }
			requests.post(NtosUrl, data=data)
			break

	if MatchChk == "n" :
		#더보기
		time.sleep(random.randint(2, 7))
		mod_more_wrap = driver.find_elements(By.CLASS_NAME, "mod_more_wrap")
		TargetClick(mod_more_wrap[0])
		ScrollDown(random.uniform(0.5, 1), 'num')
		Search1_tags_ = driver.find_elements(By.TAG_NAME, "a")

		for Val_ in Search1_tags_ :
			if Val_.text == SearchChk1 and SearchChk1 :
				TargetClick(Val_)
				MatchChk = "y"
				data = {'mode': 'up', 'type':'pc2', 'text':str(Val.text) }
				requests.post(NtosUrl, data=data)
				break

	if MatchChk == "n" :	#page 이동
		try :
			time.sleep(random.randint(2, 5))
			p_element = driver.find_element(By.CSS_SELECTOR, "a[href*='page="+str(Page)+"']")
			time.sleep(random.randint(2, 5))
			TargetClick(p_element)
			time.sleep(random.randint(2, 5))
			ScrollDown(random.uniform(0.5, 1), 'num')
			time.sleep(random.randint(2, 5))

			mecotines = driver.find_elements(By.CSS_SELECTOR, "a[href*='"+str(SearchChk2)+"']")
			mecotines_target = random.randint(0, len(mecotines)-1)
			TargetClick(mecotines[mecotines_target])
			MatchChk = "y"
		except :
			print(str(traceback.format_exc()))

	if Page == "2" and MatchChk == "n" :
		try :
			time.sleep(random.randint(2, 5))
			p_element = driver.find_element(By.CSS_SELECTOR, "a[href*='page=3']")
			time.sleep(random.randint(2, 5))
			TargetClick(p_element)
			time.sleep(random.randint(2, 5))
			ScrollDown(random.uniform(0.5, 1), 'num')
			time.sleep(random.randint(2, 5))

			mecotines1 = driver.find_elements(By.CSS_SELECTOR, "a[href*='"+str(SearchChk2)+"']")
			mecotines1_target = random.randint(0, len(mecotines1)-1)
			TargetClick(mecotines1[mecotines1_target])
			MatchChk = "y"
		except :
			print(str(traceback.format_exc()))

	if MatchChk == "n" :
		try :
			time.sleep(random.randint(2, 5))
			p_element = driver.find_element(By.CSS_SELECTOR, "a[href*='page=4']")
			time.sleep(random.randint(2, 5))
			TargetClick(p_element)
			time.sleep(random.randint(2, 5))
			ScrollDown(random.uniform(0.5, 1), 'num')
			time.sleep(random.randint(2, 5))

			mecotines2 = driver.find_elements(By.CSS_SELECTOR, "a[href*='"+str(SearchChk2)+"']")
			mecotines2_target = random.randint(0, len(mecotines2)-1)
			TargetClick(mecotines2[mecotines2_target])
			MatchChk = "y"
		except :
			print(str(traceback.format_exc()))
			
	if MatchChk == "y" :
		try :
			time.sleep(random.randint(3, 6))
			driver.switch_to.window(driver.window_handles[-1])
			time.sleep(random.randint(10, 15))
			ScrollDown(random.uniform(0.5, 1), 'num')
			time.sleep(random.randint(25, 35))

			driver.execute_script("window.scrollTo(0, 0);")
			time.sleep(random.randint(1, 2))
			h_element = driver.find_element(By.CSS_SELECTOR, "a[href='/']")
			time.sleep(random.randint(1, 3))
			h_element.click()
				
			time.sleep(random.randint(3, 7))
			ScrollDown(random.uniform(0.5, 1), 'num')
			time.sleep(random.randint(20, 60))

			conloop = random.randint(1, 2)
			if conloop == 1 :
				try :
					time.sleep(random.randint(2, 5))
					a_elements = driver.find_elements(By.CSS_SELECTOR, "a[href*='shopdetail']")
					a_emerand = random.randint(0, len(a_elements)-1)
					a_emerand_target = a_elements[a_emerand]
					TargetClick(a_emerand_target)
					time.sleep(random.randint(2, 5))
					ScrollDown(random.uniform(0.5, 1), 'num')
					time.sleep(random.randint(10, 30))
					driver.execute_script("window.history.go(-1)")
					time.sleep(random.randint(3, 7))
					ScrollDown(random.uniform(0.5, 1), 'num')
					time.sleep(random.randint(25, 40))
				except :
					print(str(traceback.format_exc()))
		except :
			print(str(traceback.format_exc()))
	print("SUCCESS")

except :
	print("FALSE")
	print(str(traceback.format_exc()))

# 종료
driver.quit()
