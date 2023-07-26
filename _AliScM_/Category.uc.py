# -*- coding: utf-8 -*- 
#알리 카테고리 모바일 uc
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

import undetected_chromedriver as uc

#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


sys.path.append(os.path.dirname("/home/ntosmini/public_html/_agent.py"))
import _agent
UserAgent = _agent.get_mobile_agent()

SiteUrlList = []

MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)

SiteUrlList = MConfig['SiteUrlList']
CustId = MConfig['CustId']
FileSendSave = MConfig['FileSendSave']  #저장후 전송여부
NtosServer = MConfig['NtosServer']  #전송서버 url
FileDir = MConfig['FileDir']  #저장폴더
LangType = MConfig['LangType']	#언어 및 통화 (ko | en)

Scroll = MConfig['Scroll']  #스크롤
StartUrl = MConfig['StartUrl']  #시작URL
ChromeVer = MConfig['ChromeVer']  #크롬버전

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
		chrome_options.add_argument('user-agent=' + UserAgent)
	if ChromeVer :
		driver = uc.Chrome(service=chrome_service, options=chrome_options, version_main=ChromeVer)
	else :
		driver = uc.Chrome(service=chrome_service, options=chrome_options, use_subprocess=True)
	return driver

driver = chromeWebdriver()

if StartUrl :
	driver.get(StartUrl)
	driver.implicitly_wait(10)

for val in SiteUrlList :
	#에러msg
	ErrMsg = ''
	PageHtml = ''
	NowUrl = ''
	(SiteUrl, SaveFileName) = val.split("|@|")
	OriginUrl = "<ntosoriginurl>"+str(SiteUrl)+"</ntosoriginurl>\n\n"
	#저장파일명
	SaveFile = FileDir+str(SaveFileName)
	SaveFile = SaveFile.replace('.html', '_'+str(time.strftime('%H%M', time.localtime(time.time())))+'.html')
	if SiteUrl == "" or SaveFileName == "" :
		pass
	else :
		try :
			driver.get(SiteUrl)
			driver.implicitly_wait(10)
			PageHtml = driver.page_source
			NowUrl = driver.current_url
		except :
			PageHtml = ''
			PageHtmlRecode = 'error'
			ErrMsg = str(traceback.format_exc())

		if NowUrl :
			NowUrl = "<ntosnowurl>"+NowUrl+"</ntosnowurl>\n\n"

		if ErrMsg :
			ErrMsg = "<error>"+ErrMsg+"</error>\n\n"
		WriteFile = "<time>"+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+"</time>\n\n"
		WriteFile = WriteFile + OriginUrl + NowUrl + PageHtml + ErrMsg

		f = open(SaveFile, 'w', encoding="utf8")
		f.write(WriteFile)
		f.close()
		os.system("gzip "+SaveFile)

		if FileSendSave == "Y" and NtosServer != "" :
			gzfile = SaveFile+".gz"
			files = open(gzfile, 'rb')
			upload = {'file': files}
			data = {'CustId':CustId, 'ScrapType':'cate' }
			Result_ = requests.post(NtosServer, data=data, files=upload)
			Result = Result_.text
			if os.path.exists(gzfile) :
				os.remove(gzfile)
	time.sleep(random.randint(3, 6))
