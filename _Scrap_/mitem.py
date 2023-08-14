# -*- coding: utf-8 -*- 

import time
import sys
import io
import random
import os
import datetime
import json
import traceback

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

sys.path.append(os.path.dirname("/home/ntosmini/public_html/_agent.py"))
import _agent
UserAgent = _agent.get_mobile_agent()


def chromeWebdriver():
	if Type == "server" :
		chrome_service = ChromeService(ChromeDriverManager(version="114.0.5735.90").install())
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
		chrome_options.add_argument('--user-agent=' + UserAgent)

		chrome_options.page_load_strategy = 'normal'
		driver = uc.Chrome(service=chrome_service, options=chrome_options, version_main=114)
	else :
		chrome_service = ChromeService(executable_path=ChromeDriverManager(version="114.0.5735.90").install())
		chrome_options = Options()
		chrome_options.add_experimental_option('detach', True)
		chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
		if Type == "pc" :
			chrome_options.add_argument('--headless')
		chrome_options.add_argument('--no-sandbox')

		#chrome_options.add_argument("window-size=1920,1080")
		chrome_options.add_argument('user-agent='+ mobile_agent)

		driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

	return driver
	
MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)

Type = MConfig['Type']
SelectHref = MConfig['SelectHref']
Search1 = MConfig['Search1']
Search2 = MConfig['Search2']
Search3 = MConfig['Search3']

if SelectHref == "n" :
	print('error')
	exit()

search1 = ''
search2 = ''
search3 = ''

if Search1 != "n" :
	search1 = Search1[random.randint(0,len(Search1)-1)]
if Search2 != "n" :
	search2 = Search2[random.randint(0,len(Search2)-1)]
if Search3 != "n" :
	search3 = Search3[random.randint(0,len(Search3)-1)]
	
driver = chromeWebdriver()
driver.delete_all_cookies()
SiteUrl = "https://m.naver.com"
driver.get(SiteUrl)
driver.implicitly_wait(10) # 처음에만 셋팅
time.sleep(random.randint(2, 5))


# 검색창 클릭

# 모바일인 경우
driver.find_element(By.XPATH, '//*[@id="MM_SEARCH_FAKE"]').click()

elem = driver.find_element(By.XPATH, '//*[@id="query"]')
time.sleep(random.randint(2, 7))

for val in list(search1) :
	elem.send_keys(str(val))
	time.sleep(random.uniform(0.1, 2))

elem.send_keys(Keys.ENTER)
time.sleep(random.randint(2, 7))

mecotine_chk = 'n'

try :
	e = driver.find_elements(By.CSS_SELECTOR, "a[href='"+str(SelectHref)+"']")
	if e :
		mecotine_chk = 'y'
	else :
		try :
			driver.find_element(By.XPATH, '//*[@class="api_more"]').click()
			time.sleep(random.randint(2, 7))
			e = driver.find_elements(By.CSS_SELECTOR, "a[href='"+str(SelectHref)+"']")
			if e :
				mecotine_chk = 'y'
			else :
				driver.execute_script("window.history.go(-1)")
		except :
			print("EXCEPT1")	
except :
	print("EXCEPT2")

if mecotine_chk == "n" and search2 != "n" :
	time.sleep(random.randint(2, 4))
	driver.find_element(By.XPATH, '//*[@id="nx_query"]').click()
	elem = driver.find_element(By.XPATH, '//*[@id="nx_query"]')
	if search1 == search2 :
		elem.clear()
	else :
		elem.send_keys(" ")
	for val2 in list(search2) :
		elem.send_keys(str(val2))
		time.sleep(random.uniform(0.1, 2))

	elem.send_keys(Keys.ENTER)
	time.sleep(random.randint(2, 7))

	try :
		e = driver.find_elements(By.CSS_SELECTOR, "a[href='"+str(SelectHref)+"']")
		if e :
			mecotine_chk = 'y'
		else :
			try :
				driver.find_element(By.XPATH, '//*[@class="api_more"]').click()
				time.sleep(random.randint(2, 7))
				e = driver.find_elements(By.CSS_SELECTOR, "a[href='"+str(SelectHref)+"']")
				if e :
					mecotine_chk = 'y'
				else :
					driver.execute_script("window.history.go(-1)")
			except :
				print("EXCEPT3")	
	except :
		print("EXCEPT4")

if mecotine_chk == "n" and search3 != "n" :
	time.sleep(random.randint(2, 4))
	driver.find_element(By.XPATH, '//*[@id="nx_query"]').click()
	elem = driver.find_element(By.XPATH, '//*[@id="nx_query"]')
	
	elem.clear()
	time.sleep(random.randint(1, 2))
	for val3 in list(search3) :
		elem.send_keys(str(val3))
		time.sleep(random.uniform(0.1, 2))
	elem.send_keys(Keys.ENTER)
	time.sleep(random.randint(2, 7))

	try :
		e = driver.find_elements(By.CSS_SELECTOR, "a[href='"+str(SelectHref)+"']")
		if e :
			mecotine_chk = 'y'
		else :
			try :
				driver.find_element(By.XPATH, '//*[@class="api_more"]').click()
				time.sleep(random.randint(2, 7))
				e = driver.find_elements(By.CSS_SELECTOR, "a[href='"+str(SelectHref)+"']")
				if e :
					mecotine_chk = 'y'
			except :
				print("EXCEPT5")			
	except :
		print("EXCEPT6")

if mecotine_chk == "y" :
	try:

		time.sleep(random.randint(2, 7))

		e[0].click()
			
		time.sleep(random.randint(20, 46))

		a_elements = driver.find_elements(By.CSS_SELECTOR, ".main_disp a[href*='shopdetail']")

		a_elements[random.randint(0, len(a_elements)-1)].click()

		time.sleep(random.randint(20, 55))

		driver.execute_script("window.history.go(-1)")

		time.sleep(random.randint(5, 12))

		print("SUCCESS")

	except:
		print("EXCEPT7")



driver.quit()


if Type == "pc" :
	_Dir_ = "C:/_Ntos_"

	Rand_hours = random.randint(5,10)
	Rand_minutes = random.randint(1,59)
	sName = "_mitem"
	sSchedule = datetime.datetime.now() + datetime.timedelta(hours=Rand_hours, minutes=Rand_minutes)

	os.system('schtasks /delete /tn '+ sName +' /f')
	time.sleep(1)

	os.system('schtasks /create /tn '+ sName +' /tr '+ _Dir_ +'/mitem.bat /sc once /st '+ sSchedule.strftime('%H:%M') +' /sd '+ sSchedule.strftime('%Y/%m/%d'))
