# -*- coding: utf-8 -*- 
#!/usr/bin/python3
import time
import sys
import codecs

import base64
from selenium import webdriver

from bs4 import BeautifulSoup

from selenium.webdriver.firefox.options import Options


options = webdriver.FirefoxOptions()

options.add_argument('-headless')

driver = webdriver.Firefox(executable_path="/usr/bin/geckodriver", firefox_options=options)
driver.get('http://ntos.co.kr')


page_html = driver.page_source
driver.quit()


html = BeautifulSoup(page_html, 'html.parser')
sys.stdout=codecs.getwriter("utf-8")(sys.stdout.detach())
print(html)