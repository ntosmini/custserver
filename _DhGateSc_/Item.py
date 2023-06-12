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
import re

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
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse, unquote

#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

SiteUrl_SaveFileName = []

MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)

CustId = MConfig['CustId']
SiteUrlOne = MConfig['SiteUrlOne']
SiteUrl_SaveFileName = MConfig['SiteUrl_SaveFileName']
Refresh = MConfig['Refresh']
Scroll = MConfig['Scroll']
ScrapResultType = MConfig['ScrapResultType']
FileSaveDir = MConfig['FileSaveDir']
NtosSendServer = MConfig['NtosSendServer']
UserAgent = MConfig['UserAgent']
ChromeVer = MConfig['ChromeVer']

executable_path = ChromeDriverManager().install()

def chromeWebdriver():
	chrome_service = ChromeService(executable_path)
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

driver.get("https://www.dhgate.com")
getcookies = driver.get_cookies()
driver.delete_all_cookies()

for cookie in getcookies :
	arr = {}
	if cookie['name'] == "b2b_ship_country" :
		cookie['value'] = "KR"
	if cookie['name'] == "b2b_ip_country" :
		cookie['value'] = "US"

	for val in cookie.keys() :
		arr[val] = cookie[val]
	driver.add_cookie(arr)
  
driver.maximize_window()

if SiteUrlOne == "N" :
	for val in SiteUrl_SaveFileName :
		PageHtml = ""
		OptHtml = ""
		NowUrl = ""
		SiteUrl = ""
		SaveFileName = ""

		try :
			(SiteUrl, SaveFileName) = val.split("|@|")
		except :
			err = traceback.format_exc()
			PageHtml = str(err)+"\n"
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
			try :
				ItemSkuSearch = re.search(r'"sku":"(?P<ItemSkuCode>[^"]+)",', str(PageHtml), re.DOTALL)
				ItemSku = ItemSkuSearch.group('ItemSkuCode')
				ItemOptUrl = "https://kr.dhgate.com/prod/ajax/pcsku.do?client=pc&language=kr&version=0.1&itemCode="+str(ItemSku)
				driver.get(ItemOptUrl)
				OptHtml = driver.page_source
			except :
				OptHtml = ""
			
		except :
			err = traceback.format_exc()
			PageHtml = PageHtml+str(err)+"\n"

		PageHtml = "<ntosoriginurl>" + str(SiteUrl) + "</ntosoriginurl>\n" + "<ntosnowurl>" + str(NowUrl) + "</ntosnowurl>\n" + "<OptHtml>" + OptHtml + "</OptHtml>\n" + PageHtml

		if ScrapResultType == "save" :
			SaveFile = str(FileSaveDir)+str(SaveFileName)
			WriteContent = PageHtml
			f = open(SaveFile, 'w', encoding="utf8")
			f.write(WriteContent)
			f.close()
			os.system("gzip "+SaveFile)
		elif ScrapResultType == "send" :
			SaveFile = str(FileSaveDir)+str(SaveFileName)
			WriteContent = PageHtml
			f = open(SaveFile, 'w', encoding="utf8")
			f.write(WriteContent)
			f.close()
			os.system("gzip "+SaveFile)

			gzfile = SaveFile+".gz"
			files = open(gzfile, 'rb')
			upload = {'file': files}
			data = {'CustId':CustId }
			Result_ = requests.post(NtosSendServer, data=data, files=upload)
			res = Result_.text
			time.sleep(3)
			os.remove(gzfile)
		else :
			pass

else :
	PageHtml = ""
	OptHtml = ""
	NowUrl = ""
	SiteUrl = str(SiteUrlOne)
	SaveFileName = ""

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

		try :
			ItemSkuSearch = re.search(r'"sku":"(?P<ItemSkuCode>[^"]+)",', str(PageHtml), re.DOTALL)
			ItemSku = ItemSkuSearch.group('ItemSkuCode')
			ItemOptUrl = "https://kr.dhgate.com/prod/ajax/pcsku.do?client=pc&language=kr&version=0.1&itemCode="+str(ItemSku)
			driver.get(ItemOptUrl)
			OptHtml = driver.page_source
		except :
			OptHtml = ""
	except :
		err = traceback.format_exc()
		PageHtml = PageHtml+str(err)+"\n"

	PageHtml = "<ntosoriginurl>" + str(SiteUrl) + "</ntosoriginurl>\n" + "<ntosnowurl>" + str(NowUrl) + "</ntosnowurl>\n" + "<OptHtml>" + OptHtml + "</OptHtml>\n" + PageHtml

	if ScrapResultType == "save" :
		SaveFile = str(FileSaveDir)+str(SaveFileName)
		WriteContent = PageHtml
		f = open(SaveFile, 'w', encoding="utf8")
		f.write(WriteContent)
		f.close()
		os.system("gzip "+SaveFile)
	elif ScrapResultType == "send" :
		SaveFile = str(FileSaveDir)+str(SaveFileName)
		WriteContent = PageHtml
		f = open(SaveFile, 'w', encoding="utf8")
		f.write(WriteContent)
		f.close()
		os.system("gzip "+SaveFile)

		gzfile = SaveFile+".gz"
		files = open(gzfile, 'rb')
		upload = {'file': files}
		data = {'CustId':CustId }
		Result_ = requests.post(NtosSendServer, data=data, files=upload)
		res = Result_.text
		time.sleep(3)
		os.remove(gzfile)
	elif ScrapResultType == "view" :
		print(PageHtml)
	else :
		pass

driver.quit()
