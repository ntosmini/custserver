# -*- coding: utf-8 -*- 
#상품 스트레이트-v4

import time
import sys
import json
import io
import os

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

"""
MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)

IslId_SiteUrl = MConfig['IslId_SiteUrl']
CustId = MConfig['CustId']
ScrapServerId = MConfig['ScrapServerId']
"""
IslId_SiteUrl.append("1|@|https://ko.aliexpress.com/item/3256802640251697.html|@|6955215")
IslId_SiteUrl.append("2|@|https://ko.aliexpress.com/item/3256804516344781.html|@|6955216")
IslId_SiteUrl.append("3|@|https://ko.aliexpress.com/item/3256804516317114.html|@|6955217")
IslId_SiteUrl.append("4|@|https://ko.aliexpress.com/item/3256803456813458.html|@|6955218")
IslId_SiteUrl.append("5|@|https://ko.aliexpress.com/item/3256803456424879.html|@|6955219")
IslId_SiteUrl.append("6|@|https://ko.aliexpress.com/item/3256804516307242.html|@|6955220")
IslId_SiteUrl.append("7|@|https://ko.aliexpress.com/item/3256804516368570.html|@|6955221")
CustId = "aliexpress"
ScrapServerId = "151"



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
item_{CustId}_{IslId}_{server_id}_{LogId}.html

상단 내용++
<ntosoriginurl></ntosoriginurl>
<ntosnowurl></ntosnowurl>
"""

for val in IslId_SiteUrl :
	(IslId, SiteUrl, LogId) = val.split("|@|")

	OriginUrl = "<ntosoriginurl>"+str(SiteUrl)+"</ntosoriginurl>"

	#저장파일명
	SaveFile = FileDir+"item_"+str(CustId)+"_"+str(IslId)+"_"+str(ScrapServerId)+"_"+str(LogId)+".html"

	if IslId == "" or SiteUrl == "" :
		f = open(SaveFile, 'w', encoding="utf8")
		f.write(OriginUrl)
		f.close()
		osgzip(SaveFile)
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

driver.quit()
