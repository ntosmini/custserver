# -*- coding: utf-8 -*- 

import time
import sys
import json
import io
import os
import re
import random
import traceback

#pip3 install undetected-chromedriver
import undetected_chromedriver as uc

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

opts = uc.ChromeOptions()

opts.add_argument('--headless')
opts.add_argument('--no-sandbox')
opts.add_argument('--blink-settings=imagesEnabled=false')

driver = uc.Chrome( options = opts )
driver.get( 'https://ko.aliexpress.com/item/1005005060506706.html' )

PageHtml = driver.page_source
NowUrl = driver.current_url

print(NowUrl)
print(PageHtml)
