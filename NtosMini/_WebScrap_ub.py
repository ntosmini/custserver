# -*- coding: utf-8 -*- 
import time
import sys
import codecs
import random
#pip install beautifulsoup4     <=> pip install bs4

SiteUrl = sys.argv[1]
WebType = sys.argv[2]
Referer = sys.argv[3]
Agent = sys.argv[4]

import base64
SiteUrl = base64.b64decode(SiteUrl).decode()
Referer = base64.b64decode(Referer).decode()
Agent = base64.b64decode(Agent).decode()


# "Chrome" or "Firefox" or "curl"
from bs4 import BeautifulSoup
sys.stdout=codecs.getwriter("utf-8")(sys.stdout.detach())

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
		if Agent == "not" :
			chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36")
		else :
			chrome_options.add_argument("user-agent="+ Agent)

		driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=chrome_options)
	else :	# 기본 : Firefox
		driver = webdriver.Firefox("/usr/bin/geckodriver")

	if Referer != "not" :
		driver.get(Referer);
		time.sleep(random.randint(1, 3))
	"""
	import re
	if re.search('aliexpress', SiteUrl) and  not re.search('/description/', SiteUrl) :
		driver.get('https://ko.aliexpress.com');
		driver.implicitly_wait(time_to_wait=3)
		flag = driver.find_element_by_xpath('//*[@id="switcher-info"]/span[1]/i')
		flag = flag.get_attribute("class")


		lan = driver.find_element_by_xpath('//*[@id="switcher-info"]/span[3]')
		lan = lan.text

		cur = driver.find_element_by_xpath('//*[@id="switcher-info"]/span[5]')
		cur = cur.text

		if flag == 'css_flag css_kr' and lan == "한국어" and cur == "USD" :
			pass
		else :

			try :
				driver.find_element_by_xpath('/html/body/div[5]/div/div/img[2]').click()
			except :
				pass
			
			try :
				driver.find_element_by_xpath('/html/body/div[4]/div/div/img[2]').click()
			except :
				pass
			
			try :
				driver.find_element_by_xpath('/html/body/div[3]/div/div/img[2]').click()
			except :
				pass
			
			try :
				driver.find_element_by_xpath('/html/body/div[2]/div/div/img[2]').click()
			except :
				pass
			
			try :
				driver.find_element_by_xpath('/html/body/div[1]/div/div/img[2]').click()
			except :
				pass

			#배송지 언어 통화 영역 클릭
			driver.find_element_by_xpath('//*[@id="nav-global"]/div[3]/div').click()
			time.sleep(1)

			#배송지 클릭
			driver.find_element_by_xpath('//*[@id="nav-global"]/div[3]/div/div/div/div[1]/div').click()
			driver.find_element_by_xpath('//*[@id="nav-global"]/div[3]/div/div/div/div[1]/div/div[1]/ul/li[109]').click()


			#언어 클릭
			driver.find_element_by_xpath('//*[@id="nav-global"]/div[3]/div/div/div/div[2]/div').click()
			driver.find_element_by_xpath('//*[@id="nav-global"]/div[3]/div/div/div/div[2]/div/ul/li[11]').click()


			#통화 클릭
			driver.find_element_by_xpath('//*[@id="nav-global"]/div[3]/div/div/div/div[3]/div').click()
			driver.find_element_by_xpath('//*[@id="nav-global"]/div[3]/div/div/div/div[3]/div/ul/li[1]').click()


			#확인
			driver.find_element_by_xpath('//*[@id="nav-global"]/div[3]/div/div/div/div[4]/button').click()
			driver.implicitly_wait(time_to_wait=3)
	else :
		pass
	"""

	driver.get(SiteUrl);
	

	"""
	#경고창
	try :
		result = driver.switch_to_alert()
#		result.accept()
		result.dismiss()
	except :
		pass
	"""



driver.implicitly_wait(4)
page_html = driver.page_source
driver.quit()
	
html = BeautifulSoup(page_html, 'html.parser')
print(html)
