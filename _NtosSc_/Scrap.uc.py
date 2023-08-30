# -*- coding: utf-8 -*- 
# 스크렙

import time
import sys
import json
import io
import os
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

import undetected_chromedriver as uc

#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

SiteUrlArr = []

MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)

SiteUrlArr = MConfig['SiteUrlArr']
FileSaveDir = MConfig['FileSaveDir']
FileSendSave = MConfig['FileSendSave']	#파일 저장 전송 사용여부 y/n
NtosServer = MConfig['NtosServer']	#받을 url

UserAgent = MConfig['UserAgent']
ChromeVer = MConfig['ChromeVer']

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
	if UserAgent :
		chrome_options.add_argument('--user-agent=' + UserAgent)
	if ChromeVer :
		driver = uc.Chrome(service=chrome_service, options=chrome_options, version_main=ChromeVer)
	else :
		driver = uc.Chrome(service=chrome_service, options=chrome_options, use_subprocess=True)
	return driver
try :
	driver = chromeWebdriver()

	for val in SiteUrlArr :
		(CustId, SiteUrl, SaveFileName) = val.split("|@|")
		OriginUrl = "<ntosoriginurl>"+str(SiteUrl)+"</ntosoriginurl>\n"

		PageHtml = ""
		NowUrl = ""
		if SiteUrl == "" or SaveFileName == "" :
			pass
		else :
			try :
				criver.get(SiteUrl)
				driver.implicitly_wait(10)
				PageHtml = driver.page_source
				NowUrl = driver.current_url
			except :
				PageHtml = str(traceback.format_exc())
			
			WriteFile = "<time>"+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+"</time>\n\n"
			WriteFile = WriteFile + str(OriginUrl)
			if NowUrl :
				WriteFile = WriteFile + "<ntosnowurl>"+NowUrl+"</ntosnowurl>\n"
			
			WriteFile = WriteFile + PageHtml

			if FileSaveDir :
				SaveFile = FileSaveDir+str(SaveFileName)
				SaveFile = SaveFile.replace('.html', '_'+str(time.strftime('%H%M', time.localtime(time.time())))+'.html')
				f = open(SaveFile, 'w', encoding="utf8")
				f.write(WriteFile)
				f.close()
				os.system("gzip "+SaveFile)

				if FileSendSave == "y" and NtosServer != "" :
					gzfile = SaveFile+".gz"
					files = open(gzfile, 'rb')
					upload = {'file': files}
					data = {'CustId':CustId, 'ScrapType':'cate' }
					Result_ = requests.post(NtosServer, data=data, files=upload)
					Result = Result_.text
					if os.path.exists(gzfile) :
						os.remove(gzfile)
			else :
				print(WriteFile)
		time.sleep(random.uniform(2, 4))
	driver.quit()
except :
	print(str(traceback.format_exc()))
