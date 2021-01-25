# -*- coding: utf-8 -*- 
import time
import sys
import codecs
#pip install beautifulsoup4     <=> pip install bs4

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
#		from pyvirtualdisplay import Display
#		display = Display(visible=0, size=(1920, 1080))  
#		display.start()

		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument("-disable-notifications")
		chrome_options.add_argument('--headless')
		chrome_options.add_argument('--no-sandbox')
		chrome_options.add_argument('--disable-dev-shm-usage')
		chrome_options.add_argument("--window-size=1920x1080")
		chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36")

		driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=chrome_options)
	else :	# 기본 : Firefox
		driver = webdriver.Firefox("/usr/bin/geckodriver")

	if Referer != "not" :
		driver.get(Referer);
		time.sleep(2)

	driver.get(SiteUrl);
	time.sleep(3)

	#경고창
	try :
		result = driver.switch_to_alert()
#		result.accept()
		result.dismiss()
	except :
		pass


	page_html = driver.page_source
	driver.quit()
	
html = BeautifulSoup(page_html, 'html.parser')
sys.stdout=codecs.getwriter("utf-8")(sys.stdout.detach())
print(html)