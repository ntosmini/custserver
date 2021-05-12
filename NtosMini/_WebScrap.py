# -*- coding: utf-8 -*- 
import time
import sys
import codecs
#pip install beautifulsoup4     <=> pip install bs4
import threading

SiteUrl = sys.argv[1]
WebType = sys.argv[2]
Referer = sys.argv[3]

import base64
SiteUrl = base64.b64decode(SiteUrl).decode()
Referer = base64.b64decode(Referer).decode()


# "Chrome" or "Firefox" or "curl"
from bs4 import BeautifulSoup

if WebType == "curl" :
	from urllib.request import urlopen
	page_html = urlopen(SiteUrl)

else :
	from selenium import webdriver
	from selenium.webdriver.common.alert import Alert

	if WebType == "Chrome" :
		driver = webdriver.Chrome("C:/xampp/htdocs/NtosMini/chromedriver.exe")
	else :	# 기본 : Firefox
		driver = webdriver.Firefox("C:/xampp/htdocs/NtosMini/geckodriver.exe")

	if Referer != "not" :
		driver.get(Referer);
		time.sleep(random.randint(1, 3))

	#종료
	def DriverQuit():
		driver.quit()
		print('')
		exit()

	DriverJob = threading.Timer(300, DriverQuit)
	DriverJob.start()

	driver.get(SiteUrl);
	time.sleep(3)

	DriverJob.cancel()


	page_html = driver.page_source
	driver.quit()
	
html = BeautifulSoup(page_html, 'html.parser')
sys.stdout=codecs.getwriter("utf-8")(sys.stdout.detach())
print(html)
