# -*- coding: utf-8 -*- 
# 사이트 배열 수집

import time
import sys
import json
import io
import os
import requests
import traceback

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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains

#pip3 install webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import undetected_chromedriver as uc

SiteUrlArr = []

MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)

SiteUrlArr = MConfig['SiteUrlArr']
CustId = MConfig['CustId']
Scroll = MConfig['Scroll']

FileSendSave = MConfig['FileSendSave']
NtosServer = MConfig['NtosServer']
UserAgent = MConfig['UserAgent']
FileSaveDir = MConfig['FileSaveDir']
ChromeVer = MConfig['ChromeVer']
StartUrl = MConfig['StartUrl']

FileDir = ""
if FileSaveDir == "" :
	exit()
else :
	FileDir = FileSaveDir


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
	if ChromeVer :
		driver = uc.Chrome(service=chrome_service, options=chrome_options, version_main=ChromeVer)
	else :
		driver = uc.Chrome(service=chrome_service, options=chrome_options, use_subprocess=True)
	return driver

driver = chromeWebdriver()

if StartUrl != "N" :
	driver.get(StartUrl)
	driver.implicitly_wait(5)

for val in SiteUrlArr : 
	(SiteUrl, SaveFileName) = val.split("|@|")
	OriginUrl = "<ntosoriginurl>"+str(SiteUrl)+"</ntosoriginurl>"
	#저장파일명
	SaveFile = FileDir+str(SaveFileName)

	PageHtml = ""
	NowUrl = ""
	if SiteUrl == "" or SaveFileName == "" :
		continue
	else :
		try :
			driver.get(SiteUrl)
			driver.implicitly_wait(5)

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

			PageHtml = driver.page_source
			NowUrl = driver.current_url
		except :
			PageHtml = traceback.format_exc()

		WriteFile = ""
		WriteFile = WriteFile + OriginUrl+"\n"

		if NowUrl :
			WriteFile = WriteFile + "<ntosnowurl>"+NowUrl+"</ntosnowurl>\n"

		WriteFile = WriteFile + PageHtml
		f = open(SaveFile, 'w', encoding="utf8")
		f.write(WriteFile)
		f.close()
		os.system("gzip "+SaveFile)

		if FileSendSave == "Y" and NtosServer != "" :
			gzfile = SaveFile+".gz"
			files = open(gzfile, 'rb')
			upload = {'file': files}
			data = {'CustId':CustId }
			Result_ = requests.post(NtosServer, data=data, files=upload)
			Result = Result_.text
			if os.path.exists(gzfile) :
				os.remove(gzfile)
driver.quit()