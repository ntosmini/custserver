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


LockChkCnt = int(0)
def LockChkAction(PageHtml) :
	global LockChkCnt
	global driver
	time.sleep(random.uniform(1, 3))
	print("-"+str(LockChkCnt)+" == ")
	if LockChkCnt > 100 :
		print(str(LockChkCnt)+" stop")
		return 'lockover'

	if LockSlider == "n" :
		return 'pass'

	ResultLockChk = "no : "+str(LockChkCnt)
	if re.search("Please refresh and try again", str(PageHtml)) :
		print("re")
		time.sleep(1)
		driver.refresh()
		LockChkCnt = LockChkCnt + 1
		driver.implicitly_wait(10)
		PageHtml1 = driver.page_source
		return LockChkAction(PageHtml1)
	action = ActionChains(driver)
	if re.search("Sorry, we have detected unusual traffic from your network", str(PageHtml)) :
		print("Sorry")
		try :
			slider = driver.find_element(By.ID, "nc_1_n1z")
			if slider :
				time.sleep(random.uniform(0.5, 2))
				slider.click()
				action.move_to_element(slider)
				action.click_and_hold(slider)
				"""
				xoffset = 0
				while xoffset < 500:
					xmove = 499	#random.randint(50, 70)
					ymove = random.randint(-1, 1)
					action.move_by_offset(xmove, ymove)
					xoffset += xmove
				"""
				action.move_by_offset(random.uniform(400, 500), random.randint(-1, 1))
				action.release()
				action.perform()
				ResultLockChk = "page ok : "+str(LockChkCnt)
				LockChkCnt = LockChkCnt + 1
				driver.implicitly_wait(10)
				PageHtml2 = driver.page_source
				return LockChkAction(PageHtml2)
		except :
			ResultLockChk = traceback.format_exc()+" : "+str(LockChkCnt)
			pass
	elif re.search(".com:443", str(PageHtml)) :
		print("com:443")
		iframe = driver.find_elements(By.TAG_NAME, "iframe")
		for iframeVal in iframe :
			driver.switch_to.frame(iframeVal)
			try :
				slider2 = driver.find_element(By.ID, "nc_1_n1z")
				if slider2 :
					time.sleep(random.uniform(0.5, 2))
					slider2.click()
					action.move_to_element(slider2)
					action.click_and_hold(slider2)
					"""
					xoffset = 0
					while xoffset < 500:
						xmove = random.randint(10, 50)
						ymove = random.randint(-1, 1)
						action.move_by_offset(xmove, ymove)
						xoffset += xmove
					"""
					action.move_by_offset(random.uniform(400, 500), random.randint(-1, 1))
					action.release()
					action.perform()
					ResultLockChk = "iframe ok : "+str(LockChkCnt)
					driver.switch_to.default_content()
					LockChkCnt = LockChkCnt + 1
					driver.implicitly_wait(10)
					PageHtml3 = driver.page_source
					return LockChkAction(PageHtml3)
			except :
				ResultLockChk = traceback.format_exc()+" : "+str(LockChkCnt)
				pass
			driver.switch_to.default_content()
	else :
		ResultLockChk = "non : "+str(LockChkCnt)
	return ResultLockChk


cookies_en = {
'xman_us_f': 'x_l=0&x_locale=en_US&x_c_chg=1&acs_rt=',
'aep_usuc_f': 'site=usa&c_tp=USD&region=US&b_locale=en_US',
'intl_locale': 'en_US'
}
cookies_ko = {
'xman_us_f': 'x_l=0&x_locale=ko_KR&x_c_chg=1&acs_rt=',
'aep_usuc_f': 'site=kor&c_tp=KRW&region=KR&b_locale=ko_KR',
'intl_locale': 'ko_KR'
}
headers = {
	"User-Agent":UserAgent
}
if StartUrl == "" :
	StartUrl = "https://m.aliexpress.com"


driver.get(StartUrl)
driver.implicitly_wait(10)
PageHtml = driver.page_source
aa = LockChkAction(PageHtml)
PageHtml1 = driver.page_source
print(str(aa))
#저장파일명
SaveFileName = "seller.ntos.co.kr_alichiadmin_item_1215184_55632007026003000000_841_not_xs438.html"
SaveFile = FileDir+str(SaveFileName)
SaveFile = SaveFile.replace('.html', '_'+str(time.strftime('%H%M', time.localtime(time.time())))+'.html')

WriteFile = "<PageHtml>"+str(PageHtml)+"</PageHtml>\n\n"+"<PageHtml1>"+str(PageHtml1)+"</PageHtml1>"

f = open(SaveFile, 'w', encoding="utf8")
f.write(WriteFile)
f.close()
os.system("gzip "+SaveFile)

if FileSendSave == "y" and NtosServer != "" :
	gzfile = SaveFile+".gz"
	files = open(gzfile, 'rb')
	upload = {'file': files}
	data = {'CustId':CustId, 'ScrapType':'item' }
	Result_ = requests.post(NtosServer, data=data, files=upload)
	Result = Result_.text
	if os.path.exists(gzfile) :
		os.remove(gzfile)


exit()



if CookiesLang :
	getcookies = driver.get_cookies()
	driver.delete_all_cookies()

	for cookie in getcookies :
		arr = {}
		parts = ''
		new_url = ''
		qs = {}
		if cookie['name'] == "aep_usuc_f" :
			parts = urlparse(StartUrl+'?'+cookie['value'])
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
			new_url = unquote(new_url.replace(StartUrl+'?', ''))
			cookie['value'] = new_url

		parts = ''
		new_url = ''
		qs = {}
		if cookie['name'] == "xman_us_f" :
			parts = urlparse(StartUrl+'?'+cookie['value'])
			qs = dict(parse_qsl(parts.query))
			if CookiesLang == "en" :
				qs['x_locale'] = 'en_US'
			elif CookiesLang == "ko" :
				qs['x_locale'] = 'ko_KR'
			parts = parts._replace(query=urlencode(qs))
			new_url = urlunparse(parts)
			new_url = unquote(new_url.replace(StartUrl+'?', ''))
			cookie['value'] = new_url

		if cookie['name'] == "intl_locale" :
			if CookiesLang == "en" :
				cookie['value'] = "en_US"
			elif CookiesLang == "ko" :
				cookie['value'] = "ko_KR"

		for val in cookie.keys() :
			arr[val] = cookie[val]
		driver.add_cookie(arr)
	time.sleep(3)
	#driver.maximize_window()



try :
	for val in SiteUrlList :
		LockChkCnt = 0
		
		LogMsg = ''
		NowUrl = ''
		ErrMsg = ''
		LockChk = ''

		PageHtml = ''
		SaveHtml = ''
		PageHtmlJson = ''
		DetailUrl = ''
		DetailHtml = ''

		(SiteUrl, SaveFileName) = val.split("|@|")
		
		OriginUrl = "<ntosoriginurl>"+str(SiteUrl)+"</ntosoriginurl>\n\n"
		#저장파일명
		SaveFile = FileDir+str(SaveFileName)
		SaveFile = SaveFile.replace('.html', '_'+str(time.strftime('%H%M', time.localtime(time.time())))+'.html')

		if SiteUrl == "" or SaveFileName == "" :
			LogMsg = LogMsg + "\ncontinue"
			continue
		else :
			try :
				driver.get(SiteUrl)
				driver.implicitly_wait(10)
				PageHtml = driver.page_source
				LockChk = LockChkAction(PageHtml)
				PageHtml = driver.page_source
				if LockChk == "lockover" :
					print("lockover continue")
					continue
				PageHtml = driver.page_source
				NowUrl = driver.current_url
			except :
				ErrMsg = ErrMsg + str(traceback.format_exc()) + "\n\n"

			if PageHtml :
				if Scroll == "y" :
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
				try :
					PageHtml = re.sub("\n", "", PageHtml)
					PageHtmlJsonSearch = re.search(r"window.runParams\s+=\s+{\s+ data:(?P<JsonData>.*)};\s+</script>", str(PageHtml), re.DOTALL)
					PageHtmlJsonData = PageHtmlJsonSearch.group("JsonData")
					PageHtmlJson = json.loads(PageHtmlJsonData)
				except :
					PageHtmlJson = ""
					ErrMsg = ErrMsg + str(traceback.format_exc()) + "\n\n"
			
			if PageHtmlJson :
				SaveHtml = SaveHtml + "<PageHtmlJson>" + str(PageHtmlJsonData) + "</PageHtmlJson>\n\n"
				try :
					DetailUrl = PageHtmlJson['descInfo']['productDescUrl']
				except :
					DetailUrl = "";
					ErrMsg = ErrMsg + str(traceback.format_exc()) + "\n\n"
				
				if DetailUrl :
					time.sleep(random.uniform(1, 3))
					try :
						if CookiesLang == "ko" :
							DetailHtml = requests.get(str(DetailUrl), headers=headers, cookies=cookies_ko)
						elif CookiesLang == "en" :
							DetailHtml = requests.get(str(DetailUrl), headers=headers, cookies=cookies_en)
						else :
							DetailHtml = requests.get(str(DetailUrl), headers=headers)
						DetailHtml = DetailHtml.text
					except :
						DetailHtml = ''
						ErrMsg = ErrMsg + str(traceback.format_exc()) + "\n\n"

					if DetailHtml == "" :
						try :
							DetailHtml = driver.get(str(DetailUrl))
							driver.implicitly_wait(10)
							DetailHtml = driver.page_source
							time.sleep(random.uniform(2, 3))
							driver.back()
						except :
							DetailHtml = ''
							ErrMsg = ErrMsg + str(traceback.format_exc()) + "\n\n"

				if DetailHtml :
					DetailHtml = re.sub('(<script[^<]+</script>)', '', DetailHtml)
					DetailHtml = re.sub('(<a[^<]+</a>)', '', DetailHtml)
					DetailHtml = re.sub('(<link[^>]+>)', '', DetailHtml)
					SaveHtml = SaveHtml + "<DetailHtml>" + str(DetailHtml) + "</DetailHtml>\n\n"

		if NowUrl :
			NowUrl = "<ntosnowurl>"+NowUrl+"</ntosnowurl>\n\n"
		if ErrMsg :
			ErrMsg = "<errmsg>"+ErrMsg+"</errmsg>\n\n"
			
		PageHtml_ = driver.page_source
		WriteFile = "<agent>"+str(UserAgent)+"</agent>\n\n"+"<time>"+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+"</time>\n\n"
		WriteFile = WriteFile + OriginUrl + NowUrl + SaveHtml + ErrMsg + "\n\n<PageHtml>"+str(PageHtml_)+"</PageHtml>\n\n"

		f = open(SaveFile, 'w', encoding="utf8")
		f.write(WriteFile)
		f.close()
		os.system("gzip "+SaveFile)

		if FileSendSave == "y" and NtosServer != "" :
			gzfile = SaveFile+".gz"
			files = open(gzfile, 'rb')
			upload = {'file': files}
			data = {'CustId':CustId, 'ScrapType':'item' }
			Result_ = requests.post(NtosServer, data=data, files=upload)
			Result = Result_.text
			if os.path.exists(gzfile) :
				os.remove(gzfile)

		time.sleep(random.uniform(1, 3))
except :
	print(str(traceback.format_exc()))

# 종료
driver.quit()
