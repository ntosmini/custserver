# -*- coding: utf-8 -*- 
# 카테고리 멀티-v4

import time
import sys
import codecs
import random
#pip install beautifulsoup4     <=> pip install bs4
import threading
import json
import re
import io
import os
import multiprocessing
import requests

#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')



try :
	os.system("killall -o 3m chrome")
	os.system("killall -o 3m chromedriver")
except :
	pass

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

#pip3 install webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

process_list = []


MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)


NtosServer = MConfig['NtosServer']
process_list = MConfig['SclId_SiteUrl']
Agent = MConfig['Agent']
CodeLen = int(MConfig['CodeLen'])
NotsKey = MConfig['NotsKey']
CustId = MConfig['CustId']


start_time = time.time()

executable_path = ChromeDriverManager().install()

def chromeWebdriver():
	chrome_service = ChromeService(executable_path)
	chrome_options = Options()
	chrome_options.add_experimental_option('detach', True)
	chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--disable-gpu')
	#chrome_options.add_argument("--blink-settings=imagesEnabled=false")
	chrome_options.add_argument("window-size=1920,1080")

	driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

	return driver

def multiSelenium(process):
	(SclId, SiteUrl, log_id) = process.split("|@|")

	driver = chromeWebdriver()
	PageHtml = ""
	NowUrl = ""
	ItemBasicUrl = ""
	Result_ = ""
	ItemList = []
	ItemContentBox = ""
	try :
		driver.get(SiteUrl)
		driver.implicitly_wait(5)
		driver.refresh()
		driver.implicitly_wait(5)

		SCROLL_PAUSE_SEC = 0.5
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

		
		PageHtml = driver.page_source
		NowUrl = driver.current_url


		if PageHtml :
			try :
				ScriptMatched = re.search('\{"mods".*\}', page_html)
				ScriptListData = ScriptMatched.group()

				ScriptListDataArr = json.loads(ScriptListData)
				for Slist in ScriptListDataArr['mods']['itemList']['content'] :
					Code1 = str(Slist['productId'])
					if len(Code1) > CodeLen :
						ItemList.append(Code1)
						
			except :
				pass


			try :
				ItemContentBox = driver.find_element(By.CLASS_NAME, "product-container")
				ATagItems = ItemContentBox.find_elements(By.TAG_NAME, 'a')

				ItemClassName = ''
				for ATI in ATagItems :
					href = ATI.get_attribute('href')
					if re.search("aliexpress.[a-zA-Z-]+/item/\d+", str(href)) :
						ItemBasicUrl = re.sub(r'(/item/.*)$', '/item/', str(href))
						ItemClassName = ATI.get_attribute('class')
						break
				if ItemClassName :
					for ATI2 in ATagItems :
						href = ATI2.get_attribute('href')
						class_ = ATI2.get_attribute('class')
						if class_ == ItemClassName and re.search("aliexpress.[a-zA-Z-]+/item/\d+", str(href)) :
							href_result = re.sub(r'(\.html.*)$', '.html', str(href))
							Code2 = re.search("\d+", href_result).group()
							if len(str(Code2)) > CodeLen :
								ItemList.append(str(Code2))

			except :
				pass


		else :
			pass


	except :
		pass

	ItemListSet = list(set(ItemList))

	if len(ItemListSet) > 0 :
		Result = "success"
	else :
		if ItemContentBox :
			Result = "notitem"
		else :
			Result = "ItemContentBox_error"

	data = {'NtosServer':str(NtosServer), 'NotsKey':NotsKey, 'CustId':CustId, 'SclId':SclId, 'Result':Result, 'ItemList': ItemListSet, 'log_id': log_id, 'ItemBasicUrl':str(ItemBasicUrl) }
	headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
	
	try :
		Result__ = requests.post(NtosServer, data=json.dumps(data), headers=headers)
		Result_ = Result__.text
	except :
		Result_ = "requests_error"

	print(Result_)
	driver.close()
	driver.quit()

if __name__ == '__main__':
	pool = multiprocessing.Pool(processes=len(process_list))
	pool.map(multiSelenium, process_list)
	print("\n\n--- %s seconds ---" % (time.time() - start_time))
	pool.close()
	pool.join()
	sys.exit()
