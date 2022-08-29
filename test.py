# -*- coding: utf-8 -*- 


#smartstore

import sys
import os
import datetime
import time
import re
import json
import random
import base64
import selenium
import io
import requests
from selenium import webdriver

from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse
srandom = int(7)
erandom = int(10)

#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

"""
try :
	os.system("killall -o 10m chrome")
	os.system("killall -o 10m chromedriver")
except :
	pass
"""
Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/5"
Proxy = "147.78.54.184:8800"
SiteUrl = "https://ko.aliexpress.com/category/153709/temperature-instruments.html?trafficChannel=main&catName=temperaturrtType=total_tranpro_desc&minPrice=369&maxPrice=370&page=1&groupsort=1&isrefine=y"
Referer = "https://ko.aliexpress.com/category/153709/temperature-instruments.html"

"""
print('<div>SiteUrl : '+SiteUrl+'</div>')
print('<div>Agent : '+Agent+'</div>')
print('<div>Proxy : '+Proxy+'</div>')
print('<div>Referer : '+Referer+'</div>')
"""


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("-disable-notifications")
#chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--window-size=1920x1080")



if Agent == "" :
	chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36")
else :
	chrome_options.add_argument("user-agent="+ Agent)


if Proxy != "" :
	PROXY = Proxy # IP:PORT or HOST:PORT
	chrome_options.add_argument('--proxy-server=%s' % PROXY)
#if Referer != "" :
	#chrome_options.add_argument('--referer=%s' % Referer)


driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)
#driver = webdriver.Chrome('C:/_Ntos/_webdriver/chromedriver.exe', chrome_options=chrome_options)



SiteUrl = "http://xstest.ntos.co.kr/ntossmm/test2.php"
driver.get(url=SiteUrl)
driver.implicitly_wait(10)
time.sleep(random.randint(3, 4))




shopping = driver.find_elements_by_class_name("shop_product")


alink = ""
for sh in shopping :
	aTag = sh.find_element_by_tag_name('a')
	href = aTag.get_attribute('href')
	if re.search("test2.php", href) :
		aTag.click()
		break


driver.implicitly_wait(10)
time.sleep(random.randint(3, 4))


print(driver.current_url)

page_html = driver.page_source
html = BeautifulSoup(page_html, 'html.parser')






#driver.find_element_by_id('test').click()

print(html)

driver.close()
exit()
