# -*- coding: utf-8 -*- 

import time
import sys
import codecs
import random
#pip install beautifulsoup4     <=> pip install bs4
import threading
import json
import re
import io
import os
import requests
import traceback
import datetime
import shutil

from urllib.parse import urlparse, parse_qsl, urlencode, urlunparse

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


#pip3 install webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import subprocess
import socket
_Port_ = "9222"
HOST = "127.0.0.1"
PORT = int(_Port_)

# Creates a new socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Try to connect to the given host and port
if sock.connect_ex((HOST, PORT)) == 0 :
	print("Port " + str(PORT) + " is open") # Connected successfully
else :
  print("Port " + str(PORT) + " is closed") # Failed to connect because port is in use (or bad host)
  path_ = "/opt/google/chrome/chrome.exe"
  sp = subprocess.Popen(str(path_)+' --remote-debugging-port='+str(PORT)+' --user-data-dir="/home/ntosmini/scrapdata/ch"')

sock.close()
exit()
def chromeWebdriver():
	chrome_service = ChromeService(ChromeDriverManager().install())
	chrome_options = Options()
	#chrome_options.add_experimental_option('detach', True)
	#chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
	chrome_options.add_experimental_option("debuggerAddress", HOST+":"+_Port_)
	chrome_options.add_argument('--headless')
	#chrome_options.add_argument('--no-sandbox')
	#chrome_options.add_argument('--blink-settings=imagesEnabled=false')
	#chrome_options.add_argument('--window-size=1920,1080')
	#chrome_options.add_argument('--disable-dev-shm-usage')
	#chrome_options.add_argument('--disable-blink-features=AutomationControlled')
	#chrome_options.add_argument('--disable-infobars')
	#chrome_options.page_load_strategy = 'normal'
	driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
	return driver

driver = chromeWebdriver()

SiteUrl = "http://ntos.co.kr";
driver.get(SiteUrl)
driver.implicitly_wait(10)
PageHtml = driver.page_source
print(PageHtml)


