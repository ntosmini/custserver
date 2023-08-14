# -*- coding: utf-8 -*- 

import time
import sys
import io
import random
import os
import datetime
import json
import traceback

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


#pip3 install webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# 파일로 접근
import undetected_chromedriver as uc

#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)

Type = MConfig['Type']
Search1 = MConfig['Search1']
Search2 = MConfig['Search2']
Search3 = MConfig['Search3']

search1 = ''
search2 = ''
search3 = ''

if Search1 != "n" :
	search1 = Search1[random.randint(0,len(Search1)-1)]

print(search1)
