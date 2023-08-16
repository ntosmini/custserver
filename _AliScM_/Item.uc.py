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
CookiesLang = MConfig['CookiesLang']	#언어 및 통화 (ko | en)

Scroll = MConfig['Scroll']  #스크롤
StartUrl = MConfig['StartUrl']  #시작URL
ChromeVer = MConfig['ChromeVer']  #크롬버전
LockSlider = MConfig['LockSlider']	#LockSlider 사용여부(y/n)

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

driver = chromeWebdriver()

#lock 체크
LockChkCnt = int(0)
def LockChk(PageHtml) :
	global LockChkCnt
	LockChkCnt = LockChkCnt + 1
	if LockSlider == "n" :
		return "pass"
	ResultLockChk = "no"
	action = ActionChains(driver)
	try :
		if re.search('Sorry, we have detected unusual traffic from your network', str(PageHtml)) :
			try :
				slider = driver.find_element(By.ID, "nc_1_n1z")
				if slider :
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
					ResultLockChk = "page ok : "+str(LockChkCnt)
					PageHtml = driver.page_source
					LockChk(PageHtml)
					return str(ResultLockChk)
			except :
				ResultLockChk = traceback.format_exc()
				pass
		if re.search('.com:443', str(PageHtml)) :
			iframe = driver.find_elements(By.TAG_NAME, "iframe")
			for iframeVal in iframe :
				driver.switch_to.frame(iframeVal)
				try :
					slider = driver.find_element(By.ID, "nc_1_n1z")
					if slider :
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
						ResultLockChk = "iframe ok : "+str(LockChkCnt)
						driver.switch_to.default_content()
						return str(ResultLockChk)
				except :
					ResultLockChk = traceback.format_exc()
					pass
				driver.switch_to.default_content()
	except :
		ResultLockChk = traceback.format_exc()
		pass
	return str(ResultLockChk)



if StartUrl :
	driver.get(StartUrl)
	driver.implicitly_wait(10)
else :
	driver.get("https://aliexpress.com")
	driver.implicitly_wait(10)

if CookiesLang :
	getcookies = driver.get_cookies()
	driver.delete_all_cookies()

	for cookie in getcookies :
		arr = {}
		parts = ''
		new_url = ''
		qs = {}
		if cookie['name'] == "aep_usuc_f" :
			parts = urlparse('https://aliexpress.com?'+cookie['value'])
			qs = dict(parse_qsl(parts.query))
			if CookiesLang == "en" :
				qs['site'] = 'usa'
				qs['c_tp'] = 'USD'
				qs['region'] = 'US'
				qs['b_locale'] = 'en_US'
			elif CookiesLang == "ko" :
				qs['site'] = 'kor'
				qs['c_tp'] = 'KRW'
				qs['region'] = 'KR'
				qs['b_locale'] = 'ko_KR'
			parts = parts._replace(query=urlencode(qs))
			new_url = urlunparse(parts)
			new_url = unquote(new_url.replace('https://aliexpress.com?', ''))
			cookie['value'] = new_url

		parts = ''
		new_url = ''
		qs = {}
		if cookie['name'] == "xman_us_f" :
			parts = urlparse('https://aliexpress.com?'+cookie['value'])
			qs = dict(parse_qsl(parts.query))
			if CookiesLang == "en" :
				qs['x_locale'] = 'en_US'
			elif CookiesLang == "ko" :
				qs['x_locale'] = 'ko_KR'
			parts = parts._replace(query=urlencode(qs))
			new_url = urlunparse(parts)
			new_url = unquote(new_url.replace('https://aliexpress.com?', ''))
			cookie['value'] = new_url

		if cookie['name'] == "intl_locale" :
			if CookiesLang == "en" :
				cookie['value'] = "en_US"
			elif CookiesLang == "ko" :
				cookie['value'] = "ko_KR"

		for val in cookie.keys() :
			arr[val] = cookie[val]
		driver.add_cookie(arr)
		#driver.maximize_window()

time.sleep(3)

try :
	for val in SiteUrlList :
		#저장html
		SaveHtml = ''
		#에러msg
		ErrMsg = ''
		
		PageHtml = ''
		PageHtmlJson = ''
		DetailUrl = ''
		DetailHtml = ''

		NowUrl = ''
		LogMsg = ''
		LockChkMsg = ''

		(SiteUrl, SaveFileName) = val.split("|@|")
		OriginUrl = "<ntosoriginurl>"+str(SiteUrl)+"</ntosoriginurl>\n\n"

		#저장파일명
		SaveFile = FileDir+str(SaveFileName)
		SaveFile = SaveFile.replace('.html', '_'+str(time.strftime('%H%M', time.localtime(time.time())))+'.html')

		if SiteUrl == "" or SaveFileName == "" :
			LogMsg = LogMsg + "\ncontinue"
		else :
			try :
				driver.get(SiteUrl)
				driver.implicitly_wait(10)
				PageHtml = driver.page_source
				LockChkMsg = LockChk(PageHtml)
				PageHtml = driver.page_source
				NowUrl = driver.current_url
			except :
				PageHtml = ''
				NowUrl = ''
				ErrMsg = ErrMsg + str(traceback.format_exc()) + "\n\n"

			if PageHtml :
				try :
					PageHtml = re.sub('\n', '', PageHtml)
					PageHtmlJsonSearch = re.search(r'window.runParams\s+=\s+{\s+ data:(?P<JsonData>.*)};\s+</script>', str(PageHtml), re.DOTALL)
					PageHtmlJsonData = PageHtmlJsonSearch.group('JsonData')
					PageHtmlJson = json.loads(PageHtmlJsonData)
				except :
					PageHtmlJson = ''
					ErrMsg = ErrMsg + str(traceback.format_exc()) + "\n\n"

			if PageHtmlJson :
				SaveHtml = SaveHtml + "<PageHtmlJson>" + str(PageHtmlJsonData) + "</PageHtmlJson>\n\n"
				try :
					DetailUrl = PageHtmlJson['descInfo']['productDescUrl']
				except :
					DetailUrl = '';
					ErrMsg = ErrMsg + str(traceback.format_exc()) + "\n\n"

				if DetailUrl :
					try :
						time.sleep(random.randint(1, 3))
						DetailHtml = driver.get(str(DetailUrl))
						driver.implicitly_wait(10)
						DetailHtmlRecode = 'ok'
						DetailHtml = driver.page_source
					except :
						DetailHtml = ''
						DetailHtmlRecode = 'error'
						ErrMsg = ErrMsg + str(traceback.format_exc()) + "\n\n"

				if DetailHtml :
					DetailHtml = re.sub('(<script[^<]+</script>)', '', DetailHtml)
					DetailHtml = re.sub('(<a[^<]+</a>)', '', DetailHtml)
					DetailHtml = re.sub('(<link[^>]+>)', '', DetailHtml)
					SaveHtml = SaveHtml + "<DetailHtml>" + str(DetailHtml) + "</DetailHtml>\n\n"

			if LockChkMsg :
				LockChkMsg = "<LockChkMsg>"+str(LockChkMsg)+"</LockChkMsg>\n\n"

			WriteFile = "<agent>"+str(UserAgent)+"</agent>\n\n"+"<time>"+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+"</time>\n\n"
			WriteFile = LockChkMsg + WriteFile + OriginUrl + SaveHtml + ErrMsg + "\n\n<PageHtml>"+str(PageHtml)+"</PageHtml>\n\n"

			f = open(SaveFile, 'w', encoding="utf8")
			f.write(WriteFile)
			f.close()
			os.system("gzip "+SaveFile)

			if FileSendSave == "Y" and NtosServer != "" :
				gzfile = SaveFile+".gz"
				files = open(gzfile, 'rb')
				upload = {'file': files}
				data = {'CustId':CustId, 'ScrapType':'item' }
				Result_ = requests.post(NtosServer, data=data, files=upload)
				Result = Result_.text
				if os.path.exists(gzfile) :
					os.remove(gzfile)

		time.sleep(random.randint(1, 3))
except :
	print(str(traceback.format_exc()))
# 종료
driver.quit()
