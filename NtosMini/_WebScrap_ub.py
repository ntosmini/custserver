# -*- coding: utf-8 -*- 
import time
import sys
import codecs
import random
#pip install beautifulsoup4     <=> pip install bs4
import threading

SiteUrl = sys.argv[1]
WebType = sys.argv[2]
Referer = sys.argv[3]
Agent = sys.argv[4]

import base64
SiteUrl = base64.b64decode(SiteUrl).decode()
Referer = base64.b64decode(Referer).decode()
Agent = base64.b64decode(Agent).decode()

import requests


# "Chrome" or "Firefox" or "curl"
from bs4 import BeautifulSoup
sys.stdout=codecs.getwriter("utf-8")(sys.stdout.detach())

if WebType == "curl" :
	from urllib.request import urlopen
	page_html = urlopen(SiteUrl)
	html = BeautifulSoup(page_html, 'html.parser')
	data = {'a_url': SiteUrl, 'a_result': '0', 'a_msg':'curl' } 
	response = requests.post('http://ali.ntos.co.kr/_uchk.php' , data=data)

	print(html)
	exit()
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
		if Agent == "not" :
			chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36")
		else :
			chrome_options.add_argument("user-agent="+ Agent)

		data = {'a_url': SiteUrl, 'a_result': '1', 'a_msg':'driver 시작전' } 
		response = requests.post('http://ali.ntos.co.kr/_uchk.php' , data=data)

		driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=chrome_options)

		data = {'a_url': SiteUrl, 'a_result': '2', 'a_msg':'driver 시작' } 
		response = requests.post('http://ali.ntos.co.kr/_uchk.php' , data=data)

	else :	# 기본 : Firefox
		driver = webdriver.Firefox("/usr/bin/geckodriver")

	if Referer != "not" :
		driver.get(Referer)
		time.sleep(random.randint(1, 3))
	

	#종료
	def DriverQuit():
		driver.quit()
		print('')
		data = {'a_url': SiteUrl, 'a_result': '999', 'a_msg':'비정상완료' } 
		response = requests.post('http://ali.ntos.co.kr/_uchk.php' , data=data)
		exit()

	DriverJob = threading.Timer(120, DriverQuit)
	DriverJob.start()
	data = {'a_url': SiteUrl, 'a_result': '3', 'a_msg':'SiteUrl 이동전' } 
	response = requests.post('http://ali.ntos.co.kr/_uchk.php' , data=data)
	driver.get(SiteUrl)
	data = {'a_url': SiteUrl, 'a_result': '4', 'a_msg':'SiteUrl 이동' } 
	response = requests.post('http://ali.ntos.co.kr/_uchk.php' , data=data)




	data = {'a_url': SiteUrl, 'a_result': '5', 'a_msg':'SiteUrl 이동 완료' } 
	response = requests.post('http://ali.ntos.co.kr/_uchk.php' , data=data)

	time.sleep(3)

	data = {'a_url': SiteUrl, 'a_result': '6', 'a_msg':'SiteUrl 대기 완료' } 
	response = requests.post('http://ali.ntos.co.kr/_uchk.php' , data=data)
	DriverJob.cancel()

	data = {'a_url': SiteUrl, 'a_result': '7', 'a_msg':'DriverJob cancel' } 
	response = requests.post('http://ali.ntos.co.kr/_uchk.php' , data=data)

	data = {'a_url': SiteUrl, 'a_result': '8', 'a_msg':'driver.quit 전' } 
	response = requests.post('http://ali.ntos.co.kr/_uchk.php' , data=data)
	page_html = driver.page_source
	driver.quit()

	data = {'a_url': SiteUrl, 'a_result': '9', 'a_msg':'driver.quit 후' } 
	response = requests.post('http://ali.ntos.co.kr/_uchk.php' , data=data)


	html = BeautifulSoup(page_html, 'html.parser')
	data = {'a_url': SiteUrl, 'a_result': '100', 'a_msg':'정상완료' } 
	response = requests.post('http://ali.ntos.co.kr/_uchk.php' , data=data)
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
