# -*- coding: utf-8 -*- 
# 스크렙

import time
import sys
import json
import io
import os
import multiprocessing
import requests
import traceback
import random

try :
	os.system("killall -o 3m chrome")
	os.system("killall -o 3m chromedriver")
except :
	pass

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#pip3 install webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

RunSiteUrl = []

MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)

RunSiteUrl = MConfig['RunSiteUrl']
CustId = MConfig['CustId']
ScrapType = MConfig['ScrapType']
Refresh = MConfig['Refresh']
Scroll = MConfig['Scroll']
FileSaveDir = MConfig['FileSaveDir']
NtosServer = MConfig['NtosServer']
NtosSendServer = MConfig['NtosSendServer']


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
	chrome_options.page_load_strategy = 'normal'
	driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
	return driver

driver = chromeWebdriver()

for val in RunSiteUrl :
	PageHtml = ""
	NowUrl = ""
	SiteUrl = ""

	try :
		(SiteUrl, SaveFileName) = val.split("|@|")
	except :
		err = traceback.format_exc()
		PageHtml = str(err)

	if SiteUrl and SaveFileName :
		try :
			driver.get(SiteUrl)
			driver.implicitly_wait(10)

			if Refresh == "Y" :
				driver.refresh()
				driver.implicitly_wait(10)

			if Scroll == "Y" :
				SCROLL_PAUSE_SEC = 0.5
				# 스크롤 높이 가져옴
				last_height = driver.execute_script("return document.body.scrollHeight")
				while True:
					# 끝까지 스크롤 다운
					driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
					# SCROLL_PAUSE_SEC 초 대기
					time.sleep(SCROLL_PAUSE_SEC)
					# 스크롤 다운 후 스크롤 높이 다시 가져옴
					new_height = driver.execute_script("return document.body.scrollHeight")
					if new_height == last_height:
						break
					last_height = new_height
	  

			time.sleep(random.randint(1, 3))
			PageHtml = driver.page_source
			NowUrl = driver.current_url
		except :
			err = traceback.format_exc()
			PageHtml = str(err)

	PageHtml = "<ntosoriginurl>"+str(SiteUrl)+"</ntosoriginurl>\n"+ "<ntosnowurl>"+str(NowUrl)+"</ntosnowurl>\n" + PageHtml
	headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
	SaveFileName = str(NtosServer)+"_"+str(CustId)+"_"+str(ScrapType)+"_"+str(SaveFileName)


	if FileSaveDir and SaveFileName :
		SaveFile = str(FileSaveDir)+str(SaveFileName)
		WriteContent = PageHtml
		f = open(SaveFile, 'w', encoding="utf8")
		f.write(WriteContent)
		f.close()

		os.system("gzip "+SaveFile)

		gzfile = SaveFile+".gz"
		files = open(gzfile, 'rb')
		upload = {'file': files}
		data = {'CustId':CustId, 'ScrapType':'item' }
		Result_ = requests.post(NtosSendServer, data=data, files=upload)
		res = Result_.text
		time.sleep(3)
		os.remove(gzfile)
	else :
		data = {'CustId':CustId, 'ScrapType':str(ScrapType), 'PageHtml':str(PageHtml), 'SaveFileName':str(SaveFileName) }
		res = requests.post(NtosSendServer, data=json.dumps(data), headers=headers)
driver.quit()
