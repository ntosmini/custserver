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

	driver.get("https://login.aliexpress.com/?return_url=https%3A%2F%2Fm.aliexpress.us%2Faccount%2Findex.html")

	driver.implicitly_wait(10)

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
	try :
		action = ActionChains(driver)
		iframe = driver.find_element(By.XPATH, '//*[@id="baxia-dialog-content"]')
		driver.switch_to.frame(iframe)
		slider = driver.find_element(By.ID, "nc_1_n1z")
		action.move_to_element(slider)
		action.click_and_hold(slider)
		action.move_by_offset(random.uniform(300, 350), random.randint(-1, 1))
		action.release()
		action.perform()
		driver.switch_to.default_content()
		driver.implicitly_wait(10)
	except :
		print(str(traceback.format_exc()))
	# id="nc_1_n1z"
	# id="baxia-dialog-content"

	time.sleep(random.uniform(1, 3))
	driver.get("https://m.aliexpress.us/")
	driver.implicitly_wait(10)
	PageHtml11 = driver.page_source

	print(str(PageHtml11))
	exit()
	SiteUrlList = [
	"https://m.aliexpress.us/item/1005001929718955.html|@|seller.ntos.co.kr_alichiadmin_item_1215184_55632007026003000000_841_not_xs438_1.html"
	,"https://m.aliexpress.us/item/1005005340674498.html|@|seller.ntos.co.kr_alichiadmin_item_1215184_55632007026003000000_841_not_xs438_2.html"
	]
	CustId = "alichiadmin"
	FileDir = "/home/ntosmini/scrapdata/"
	NtosServer = "http://seller.ntos.co.kr/_AliWb_/ScrapSaveFile.php"
	for Val in SiteUrlList :
		(StartUrl, SaveFileName) = Val.split("|@|")

		driver.get(StartUrl)
		driver.implicitly_wait(10)
		PageHtml = driver.page_source
		NowUrl = driver.current_url

		SaveFile = FileDir+str(SaveFileName)
		SaveFile = SaveFile.replace('.html', '_'+str(time.strftime('%H%M', time.localtime(time.time())))+'.html')

		WriteFile = str(NowUrl)+"\n\n"+str(PageHtml)+"\n\n\n===========================\n\n"+str(PageHtml11)
		f = open(SaveFile, 'w', encoding="utf8")
		f.write(WriteFile)
		f.close()
		os.system("gzip "+SaveFile)

		gzfile = SaveFile+".gz"
		files = open(gzfile, 'rb')
		upload = {'file': files}
		data = {'CustId':CustId, 'ScrapType':'item' }
		Result_ = requests.post(NtosServer, data=data, files=upload)
		Result = Result_.text
		if os.path.exists(gzfile) :
			os.remove(gzfile)
		time.sleep(3)
except :
	print(str(traceback.format_exc()))
driver.quit()
