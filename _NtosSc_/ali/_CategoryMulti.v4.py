# -*- coding: utf-8 -*- 
# 카테고리 멀티-v4

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
import multiprocessing
import requests
import traceback
#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


try :
	os.system("killall -o 3m chrome")
	os.system("killall -o 3m chromedriver")
except :
	pass

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

#pip3 install webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

process_list = []


MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)


NtosServer = MConfig['NtosServer']
process_list = MConfig['CslId_SiteUrl']
Agent = MConfig['Agent']
NotsKey = MConfig['NotsKey']
CustId = MConfig['CustId']
Scroll = MConfig['Scroll']
Refresh = MConfig['Refresh']
TimeChk = MConfig['TimeChk']
Referer = MConfig['Referer']

print(NtosServer)
