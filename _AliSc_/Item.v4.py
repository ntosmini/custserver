# -*- coding: utf-8 -*- 
#상품 스트레이트-v4

import time
import sys
import json
import io
import os
import requests

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




FileDir = ""
if CustId == "aliexpress" :
	FileDir = "/home/ntosmini/ali_item_en/"
elif CustId == "aliexpresskr" :
	FileDir = "/home/ntosmini/ali_item_kr/"
else :
	print("allerror")
	exit()


def osgzip(File) :
	os.system("gzip "+File)

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

wait = WebDriverWait(driver, 10, 1)

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
	if SiteUrl == "" or SaveFileName == "" :
		continue
	else :
		try :
			driver.get(SiteUrl)
			wait.until( EC.presence_of_element_located((By.CLASS_NAME, "logo-base")) )
			#driver.execute_script("window.stop();")
			PageHtml = driver.page_source
			NowUrl = driver.current_url
		except :
			PageHtml = ""
			NowUrl = ""
		WriteFile = ""
		WriteFile = WriteFile + OriginUrl+"\n"
		if NowUrl :
			WriteFile = WriteFile + "<ntosnowurl>"+NowUrl+"</ntosnowurl>\n"
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
