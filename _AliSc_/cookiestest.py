# -*- coding: utf-8 -*- 
# 카테고리 파일-v4

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


	CookiesLang = "ko"	#MConfig['CookiesLang']	#en / ko
	FileSaveDir = "Y"	#MConfig['FileSaveDir']
	Scroll = "N"
	FileDir = ""




	def chromeWebdriver():
		chrome_service = ChromeService(ChromeDriverManager().install())
		chrome_options = uc.ChromeOptions()
		#chrome_options.add_argument('--headless')
		chrome_options.add_argument('--no-sandbox')
		chrome_options.add_argument('--blink-settings=imagesEnabled=false')
		chrome_options.add_argument('--start-maximized')
		chrome_options.add_argument('--disable-dev-shm-usage')
		chrome_options.add_argument('--disable-blink-features=AutomationControlled')
		chrome_options.add_argument('--disable-infobars')
		chrome_options.add_argument('--ignore-certificate-errors')
		chrome_options.add_argument('--ignore-ssl-errors=yes')
		chrome_options.add_argument('--disable-gpu')
		driver = uc.Chrome(service=chrome_service, options=chrome_options, use_subprocess=True)
		return driver

	driver = chromeWebdriver()

	driver.get("https://aliexpress.com")
	getcookies = driver.get_cookies()
	driver.delete_all_cookies()

	for cookie in getcookies :
		arr = {}
		parts = ''
		new_url = ''
		qs = {}
		if cookie['name'] == "aep_usuc_f" :
			# site=kor&c_tp=KRW&region=KR&b_locale=ko_KR
			#print(cookie['value']+" --- <br>")
			#cookie['value'] = cookie['value'].replace("\®", '')
			#cookie['value'] = 'site=kor&c_tp=KRW®ion=KR&b_locale=ko_KR'
			parts = urlparse('https://aliexpress.us?'+cookie['value'])
			qs = dict(parse_qsl(parts.query))
			#qs['c_tp'] = unquote(qs['c_tp'])
			if CookiesLang == "en" :
				qs['site'] = 'usa'
				qs['c_tp'] = 'USD'
				qs['region'] = 'US'
				qs['b_locale'] = 'en_US'
			elif CookiesLang == "ko" :
				qs['site'] = 'kor'
				qs['c_tp'] = 'KRW'
				qs['region'] = 'KR'
				#qs['c_tp'] = 'KRW®ion=KR'
				qs['b_locale'] = 'ko_KR'

			parts = parts._replace(query=urlencode(qs))
			new_url = urlunparse(parts)
			new_url = unquote(new_url.replace('https://aliexpress.us?', ''))
			cookie['value'] = new_url

		if cookie['name'] == "intl_locale" :
			#cookie['value'] = 'ko_KR'
			if CookiesLang == "en" :
				cookie['value'] = "en_US"
			elif CookiesLang == "ko" :
				cookie['value'] = "ko_KR"

		parts = ''
		new_url = ''
		qs = {}
		if cookie['name'] == "xman_us_f" :
			#cookie['value'] = 'x_l=0&x_locale=ko_KR&x_c_chg=1&acs_rt='
			parts = urlparse('https://aliexpress.us?'+cookie['value'])
			qs = dict(parse_qsl(parts.query))
			if CookiesLang == "en" :
				qs['x_locale'] = 'en_US'
			elif CookiesLang == "ko" :
				qs['x_locale'] = 'ko_KR'

			parts = parts._replace(query=urlencode(qs))
			new_url = urlunparse(parts)
			new_url = unquote(new_url.replace('https://aliexpress.us?', ''))
			cookie['value'] = new_url

		for val in cookie.keys() :
			arr[val] = cookie[val]
		driver.add_cookie(arr)

	"""
	파일명
	cate_{CustId}_{CslId}_{CaId}_{server_id}_{LogId}.html

	상단 내용++
	<ntosoriginurl></ntosoriginurl>
	<ntosnowurl></ntosnowurl>
	"""

	driver.maximize_window()
	try :
		OriginUrl = ""
		SiteUrl = "https://www.aliexpress.com/category/200218542/electric-window-cleaners.html?shipFromCountry=CN&CatId=200218542&trafficChannel=main&isCategoryBrowse=true&minPrice=10&maxPrice=11&g=y&isrefine=y&page=1"
		SaveFileName = "a"

		OriginUrl = "<ntosoriginurl>"+str(SiteUrl)+"</ntosoriginurl>"
		#저장파일명
		#SaveFile = FileDir+str(SaveFileName)
		ErrHtml = ''
		if SiteUrl == "" or SaveFileName == "" :
			print("aaa")
		else :
			try :
				driver.get(SiteUrl)
				#driver.execute_script("window.stop();")
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
				PageHtml = ""
				NowUrl = ""
				ErrHtml = traceback.format_exc()


			WriteFile = ""
			WriteFile = WriteFile + OriginUrl+"\n"
			if NowUrl :
				WriteFile = WriteFile + "<ntosnowurl>"+NowUrl+"</ntosnowurl>\n"
			WriteFile = WriteFile + PageHtml
			if ErrHtml :
				WriteFile = WriteFile + "\n\n" + str(ErrHtml)
			print(WriteFile)

	except :
		ErrHtml = traceback.format_exc()
		print("Error "+str(ErrHtml))
	driver.quit()
except :
	ErrHtml = traceback.format_exc()
	print("Error "+str(ErrHtml))
