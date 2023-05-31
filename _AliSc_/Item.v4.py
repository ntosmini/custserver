# -*- coding: utf-8 -*- 
#상품 스트레이트-v4

import time
import sys
import json
import io
import os
import requests
import traceback

import undetected_chromedriver as uc
from fake_useragent import UserAgent

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.action_chains import ActionChains

#pip3 install webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

try :
	os.system("killall -o 3m chrome")
	os.system("killall -o 3m chromedriver")
except :
	pass

IslId_SiteUrl = []


MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)

IslId_SiteUrl = MConfig['IslId_SiteUrl']
CustId = MConfig['CustId']

FileSendSave = MConfig['FileSendSave']
NtosServer = MConfig['NtosServer']
UserAgent = MConfig['UserAgent']



FileDir = ""
if CustId == "aliexpress" :
	FileDir = "/home/ntosmini/ali_item_en/"
elif CustId == "aliexpresskr" :
	FileDir = "/home/ntosmini/ali_item_kr/"
else :
	exit()


def osgzip(File) :
	os.system("gzip "+File)

executable_path = ChromeDriverManager().install()

def chromeWebdriver():
	ua = UserAgent()
	chrome_service = ChromeService(ChromeDriverManager().install())
	chrome_options = Options()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--blink-settings=imagesEnabled=false')
	chrome_options.add_argument('--window-size=1920,1080')
	chrome_options.add_argument('--disable-dev-shm-usage')
	chrome_options.add_argument('--disable-blink-features=AutomationControlled') # 이걸로도 되네?
	chrome_options.add_argument('--disable-infobars')
	chrome_options.add_argument('--user-agent=' + ua.random)
	chrome_options.page_load_strategy = 'normal'
	driver = uc.Chrome(service=chrome_service, options=chrome_options, version_main=113)
	return driver

driver = chromeWebdriver()
driver.delete_all_cookies()

driver.get("https://aliexpress.com")
driver.implicitly_wait(3)

#lock 체크
def LockChk(PageHtml) :
	action = ActionChains(driver)
	try :
		if re.search('.com:443/display', str(PageHtml)) :
			try :
				driver.switch_to.frame("baxia-dialog-content")
				slider = driver.find_element(By.ID, "nc_1_n1z")
				slider.click()
				action.move_to_element(slider)
				action.click_and_hold(slider)
				xoffset = 0
				while xoffset < 400 :
					xmove = random.randint(10, 50)
					ymove = random.randint(-1, 1)
					action.move_by_offset(xmove, ymove)
					xoffset += xmove
				action.release()
				action.perform()
				return "iframe"
			except :
				err = traceback.format_exc()
				return str(err)
		else :
			pass
	except :
		pass

	try :
		if re.search('Sorry, we have detected unusual traffic from your network', str(PageHtml)) :
			try :
				slider2 = driver.find_element(By.ID, "nc_1_n1z")
				slider2.click()
				action.move_to_element(slider2)
				action.click_and_hold(slider2)
				xoffset = 0
				while xoffset < 400 :
					xmove = random.randint(10, 50)
					ymove = random.randint(-1, 1)
					action.move_by_offset(xmove, ymove)
					xoffset += xmove
				action.release()
				action.perform()
				return "page"
			except :
				err = traceback.format_exc()
				return str(err)
		else :
			pass
	except :
		pass
	return "pass"

"""
파일명
item_{CustId}_{IslId}_{CaId}_{server_id}_{LogId}.html

상단 내용++
<ntosoriginurl></ntosoriginurl>
<ntosnowurl></ntosnowurl>
"""

for val in IslId_SiteUrl :
	(SiteUrl, SaveFileName) = val.split("|@|")
	OriginUrl = "<ntosoriginurl>"+str(SiteUrl)+"</ntosoriginurl>"
	#저장파일명
	SaveFile = FileDir+str(SaveFileName)
	SaveFile = SaveFile.replace('.html', '_'+str(time.strftime('%H%M', time.localtime(time.time())))+'.html')
	#에러msg
	ErrMsg = ''
	if SiteUrl == "" or SaveFileName == "" :
		continue
	else :
		try :
			driver.get(SiteUrl)
			driver.implicitly_wait(3)
			#driver.execute_script("window.stop();")
			PageHtml = driver.page_source
			NowUrl = driver.current_url
		except :
			PageHtml = ""
			NowUrl = ""
			ErrMsg = traceback.format_exc()
		WriteFile = "<time>"+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))+"</time>\n"
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
			data = {'CustId':CustId, 'ScrapType':'item' }
			Result_ = requests.post(NtosServer, data=data, files=upload)
			Result = Result_.text
			if os.path.exists(gzfile) :
				os.remove(gzfile)
driver.quit()
