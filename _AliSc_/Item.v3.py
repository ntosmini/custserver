# -*- coding: utf-8 -*- 
#상품 스트레이트-v3

import time
import sys
import json
import io
import os
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
ScrapServerId = MConfig['ScrapServerId']

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


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("-disable-notifications")
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36")
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument('--disable-infobars')
chrome_options.page_load_strategy = 'normal'

driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=chrome_options)

wait = WebDriverWait(driver, 10, 1)

"""
파일명
item_{CustId}_{IslId}_{server_id}.html

상단 내용++
<ntosoriginurl></ntosoriginurl>
<ntosnowurl></ntosnowurl>
"""

for val in IslId_SiteUrl :
	(IslId, SiteUrl) = val.split("|@|")

	OriginUrl = "<ntosoriginurl>"+str(SiteUrl)+"</ntosoriginurl>"

	#저장파일명
	SaveFile = FileDir+"item_"+str(CustId)+"_"+str(IslId)+"_"+str(ScrapServerId)+".html"

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
