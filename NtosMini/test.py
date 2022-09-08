# -*- coding: utf-8 -*- 
import time
import sys
import codecs
import random
#pip install beautifulsoup4     <=> pip install bs4
import threading

import base64
SiteUrl = "http://ntos.co.kr"
Referer = "not"
Agent = "not"
WebType = "Chrome"


# "Chrome" or "Firefox" or "curl"
from bs4 import BeautifulSoup
sys.stdout=codecs.getwriter("utf-8")(sys.stdout.detach())

if WebType == "curl" :
	from urllib.request import urlopen
	page_html = urlopen(SiteUrl)
	html = BeautifulSoup(page_html, 'html.parser')

	print(html)
	exit()
else :
	from selenium import webdriver
	from selenium.webdriver.common.alert import Alert

	if WebType == "Chrome" :
		#from pyvirtualdisplay import Display
		#display = Display(visible=0, size=(1920, 1080))  
		#display.start()


		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_argument("-disable-notifications")
		chrome_options.add_argument('--headless')
		chrome_options.add_argument('--no-sandbox')
		chrome_options.add_argument('--disable-dev-shm-usage')
		chrome_options.add_argument("--window-size=1920x1080")
		if Agent == "not" :
			chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36")
		else :
			chrome_options.add_argument("user-agent="+ Agent)


		driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=chrome_options)


	else :	# 기본 : Firefox
		driver = webdriver.Firefox("/usr/bin/geckodriver")

	if Referer != "not" :
		driver.get(Referer)
		time.sleep(random.randint(1, 3))
	

	#종료
	def DriverQuit():
		driver.quit()
		print('')
		exit()

	DriverJob = threading.Timer(300, DriverQuit)
	DriverJob.start()

	driver.get(SiteUrl)


	time.sleep(3)

	DriverJob.cancel()


	page_html = driver.page_source
	driver.quit()

	html = BeautifulSoup(page_html, 'html.parser')
	print(html)
	exit()



	"""
	#경고창
	try :
		result = driver.switch_to_alert()
		#result.accept()
		result.dismiss()
	except :
		pass
	"""
