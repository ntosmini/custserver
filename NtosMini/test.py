# -*- coding: utf-8 -*- 
#!/usr/bin/python3
import time
import sys
import codecs

import base64

SiteUrl = sys.argv[1]
SiteUrl = base64.b64decode(SiteUrl).decode()


from selenium import webdriver

from bs4 import BeautifulSoup


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("-disable-notifications")
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36")


driver = webdriver.Chrome("/usr/bin/chromedriver", chrome_options=chrome_options)

if SiteUrl == "not" :
	driver.get('http://ntos.co.kr')
else :
	driver.get(SiteUrl)


page_html = driver.page_source
driver.quit()


html = BeautifulSoup(page_html, 'html.parser')
sys.stdout=codecs.getwriter("utf-8")(sys.stdout.detach())
print(html)