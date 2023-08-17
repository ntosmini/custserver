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

path_ = ChromeDriverManager().install()
PORT = "9222"
sp = subprocess.Popen(str(path_)+' --remote-debugging-port='+str(PORT)+' --user-data-dir="/home/ntosmini/scrapdata/ch"')
