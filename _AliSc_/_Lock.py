# -*- coding: utf-8 -*- 

import time
import sys
import json
import io
import os
import re
import random
import traceback


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

#pip3 install webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

def LockChk(PageHtml) :
	action = ActionChains(driver)
	try :
		if re.search('.com:443/display', str(PageHtml)) :
			try :
				driver.switch_to.frame("baxia-dialog-content")
				clickable = driver.find_element(By.ID, "nc_1_n1z")
				(
				action.move_to_element(clickable)
					.pause(3)
					.click_and_hold()
					.pause(3)
					.drag_and_drop_by_offset(clickable, 600, 0)
					.perform()
				)
				return "iframe"
			except :
				err = traceback.format_exc()
				return str(err)
		else :
			pass
	except :
		pass

	try :
		if re.search('Sorry, we have detected unusual traffic from your network', str(PageHtml)) :
			"""
			try :
				clickable = driver.find_element(By.ID, "nc_1_n1z")
				(
				action.move_to_element(clickable)
					.pause(3)
					.click_and_hold()
					.pause(3)
					.drag_and_drop_by_offset(clickable, 600, 0)
					.perform()
				)
				time.sleep(random.randint(2, 3))
				driver.refresh()
				driver.implicitly_wait(10)
				return "page"
			except :
				err = traceback.format_exc()
				return str(err)
			"""
			try :
				slider = driver.find_element(By.ID, "nc_1_n1z")
				slider.click()
				action.move_to_element(slider)
				action.click_and_hold(slider)
				xoffset = 0
				while xoffset < 350 :
					xmove = random.randint(10, 50)
					ymove = random.randint(-1, 1)
					action.move_by_offset(xmove, ymove)
					xoffset += xmove
				action.release()
				action.perform()
				time.sleep(3)
				return "page"
			except :
				err = traceback.format_exc()
				return str(err)
		else :
			pass
	except :
		pass
	return "pass"


MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)

UserAgent = MConfig['UserAgent']
SiteUrl = MConfig['SiteUrl']
LockChkUsed = MConfig['LockChkUsed']

executable_path = ChromeDriverManager().install()

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
	chrome_options.add_argument('user-agent=' + UserAgent)
	chrome_options.page_load_strategy = 'normal'
	driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
	return driver

driver = chromeWebdriver()

if re.search('aliexpress', str(SiteUrl)) :
	driver.get("https://aliexpress.com")
	driver.implicitly_wait(10)



driver.get(SiteUrl)
driver.implicitly_wait(10)
time.sleep(random.randint(1, 3))

PageHtml = driver.page_source
NowUrl = driver.current_url
Ret = "N"
if LockChkUsed == "Y" :
	Ret = LockChk(PageHtml)
	time.sleep(random.randint(1, 3))
	PageHtml = driver.page_source
	NowUrl = driver.current_url

print(NowUrl + " = "+str(Ret))
print(PageHtml)

driver.quit()
