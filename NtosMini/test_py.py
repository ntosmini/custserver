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



# "Chrome" or "Firefox" or "curl"
from bs4 import BeautifulSoup
sys.stdout=codecs.getwriter("utf-8")(sys.stdout.detach())

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("-disable-notifications")
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36")
driver = webdriver.Chrome("/home/ntosmini/public_html/NtosMini/chromedriver", chrome_options=chrome_options)

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
