# -*- coding: utf-8 -*- 
# 카테고리 파일-v4

import time
import sys
import json
import io
import os
import requests
import traceback
import re
import random

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

from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse, unquote

CslId_SiteUrl = []


MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)

CslId_SiteUrl = MConfig['CslId_SiteUrl']
CustId = MConfig['CustId']
Scroll = MConfig['Scroll']

FileSendSave = MConfig['FileSendSave']
NtosServer = MConfig['NtosServer']
UserAgent = MConfig['UserAgent']
CookiesLang = MConfig['CookiesLang']	#en / ko
FileSaveDir = MConfig['FileSaveDir']
ChromeVer = MConfig['ChromeVer']
FileDir = ""
if FileSaveDir == "" :
	exit()
else :
	FileDir = FileSaveDir


def osgzip(File) :
	os.system("gzip "+File)

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

#lock 체크
LockChkCnt = int(0)
def LockChk(PageHtml) :
	global LockChkCnt
	action = ActionChains(driver)
	PageChk = "N"
	ResultChk = ""
	try :
		if re.search('we have detected unusual traffic from your network', str(PageHtml)) :
			PageChk = "Y"
			LockChkCnt = LockChkCnt + 1
			try :
				slider = driver.find_element(By.ID, "nc_1_n1z")
				slider.click()
				action.move_to_element(slider)
				action.click_and_hold(slider)
				xoffset = 0
				while xoffset < 500:
					xmove = random.randint(10, 50)
					ymove = random.randint(-1, 1)
					action.move_by_offset(xmove, ymove)
					xoffset += xmove
				action.release()
				action.perform()
				ResultChk = "page"
			except :
				ResultChk = traceback.format_exc()
		else :
			ResultChk = "pass"
	except :
		ResultChk = traceback.format_exc()

	if ResultChk != "page" :
		try :
			if re.search('.com:443/display', str(PageHtml)) :
				PageChk = "Y"
				LockChkCnt = LockChkCnt + 1
				try :
					driver.switch_to.frame("baxia-dialog-content")
					slider = driver.find_element(By.ID, "nc_1_n1z")
					slider.click()
					action.move_to_element(slider)
					action.click_and_hold(slider)
					xoffset = 0
					while xoffset < 500:
						xmove = random.randint(10, 50)
						ymove = random.randint(-1, 1)
						action.move_by_offset(xmove, ymove)
						xoffset += xmove
					action.release()
					action.perform()
					ResultChk = "iframe"
				except :
					ResultChk = traceback.format_exc()
			else :
				ResultChk = "pass"
		except :
			ResultChk = traceback.format_exc()

	PageHtml2 = driver.page_source

	if ResultChk != "pass" and LockChkCnt < 5 :
		LockChk(PageHtml2)

	return str(ResultChk)+" - "+str(PageChk)+" - "+str(LockChkCnt)
	
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
		print(cookie['value']+" --- <br>")
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


for val in CslId_SiteUrl :
	(SiteUrl, SaveFileName) = val.split("|@|")
	OriginUrl = "<ntosoriginurl>"+str(SiteUrl)+"</ntosoriginurl>"
	#저장파일명
	SaveFile = FileDir+str(SaveFileName)
	ErrMsg = ''
	if SiteUrl == "" or SaveFileName == "" :
		pass
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
		if ErrMsg :
			WriteFile = WriteFile + "<ErrMsg>"+str(ErrMsg)+"</ErrMsg>\n"

		#lock 체크
		if PageHtml != "" :
			lock_chk = ""
			lock_chk = LockChk(PageHtml)
			if lock_chk != "" :
				WriteFile = WriteFile + "<lock_chk>"+lock_chk+"</lock_chk>\n"

			driver.implicitly_wait(10)
			PageHtml = driver.page_source
			NowUrl = driver.current_url
		
		WriteFile = WriteFile + PageHtml
		f = open(SaveFile, 'w', encoding="utf8")
		f.write(WriteFile)
		f.close()
		osgzip(SaveFile)
		if FileSendSave == "Y" and NtosServer != "" :
			gzfile = SaveFile+".gz"
			files = open(gzfile, 'rb')
			upload = {'file': files}
			data = {'CustId':CustId, 'ScrapType':'cate' }
			Result_ = requests.post(NtosServer, data=data, files=upload)
			Result = Result_.text
			if os.path.exists(gzfile) :
				os.remove(gzfile)
driver.quit()
