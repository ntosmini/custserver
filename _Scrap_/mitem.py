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

def get_mobile_agent():
	list = ["Mozilla/5.0 (Linux; Android 13; SM-S901U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.63 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 13; Pixel 4 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.115 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5238.167 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 13; SM-S901U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 13; SM-S901U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5218.213 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 13; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 13; SM-A536E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.54 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-N986U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.115 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.15 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 13; Pixel 4 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.121 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 13; SM-S906E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.115 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 13; SM-G996B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4087.0 Mobile Safari/537.36 AlohaBrowser/4.4.4"
	,"Mozilla/5.0 (Linux; Android 13; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.125 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 13; SM-N986U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.110 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 13; Pixel 4 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.63 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 13; SM-G988B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.91 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 13; SM-A536E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; CPH2173) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; motorola edge 20 pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5170.203 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A725M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4844.73 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; V2110) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.34 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.119 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; moto e22i Build/SOW32.121-15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A135F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.110 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-M526BR) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.114 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.91 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; ko-KR; CPH2043 Build/JOP24G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.81 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5180.177 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; fr-CI; Mi 11 Lite Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.90 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.12.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; M2007J17G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5199.205 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-VE; POCO F4 GT Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.128 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.16.3.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-A715F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.114 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A515F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.91 Mobile Safari/537.36 OPX/1.7"
	,"Mozilla/5.0 (Linux; Android 12; M1908C3JGG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-SA; SM-G975U Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.4.0.1306 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; moto g(50) 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.103 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.118 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-T220) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4844.74 Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; de-DE; Mi 10T Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.75 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; LE2113) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5238.167 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; V2035) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.78 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A528B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.65 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; ko-KR; Mi 10T Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.133 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4844.51 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; fr-FR; Redmi Note 10 Pro Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.114 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-G781V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.170 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-T505) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4844.73 Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S906E) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4844.94 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2101K7BL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.9999.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A235M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.126 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; 2201116SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; zh-CN; M2003J15SC Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.70 UCBrowser/13.4.0.1306 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; 2201116TG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; V2058) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.124 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A715F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.110 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A715F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.87 Mobile Safari/537.36 EdgA/107.0.1418.28"
	,"Mozilla/5.0 (Linux; Android 12; 2201116PG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-BO; CPH2365 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 UCBrowser/13.4.0.1306 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; de-DE; Infinix X676B Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.157 HiBrowser/v2.6.3.1 UWS/ Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-G988B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.48 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-G9910) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.115 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; fr-FR; Redmi Note 11 Build/SKQ1.211103.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.56 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.14.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-A125M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; RMX2155) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.121 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-LA; POCO X3 NFC Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.18.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; LM-K500) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5206.172 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-S515DL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.170 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A217F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.119 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-GQ; Redmi Note 9S Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.64 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.14.0-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; fr-CA; Redmi Note 10 Pro Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.69 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; pt-PT; Mi Note 10 Lite Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.82 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; fr-FR; Redmi Note 10S Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.162 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.15.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; vivo 1907_19) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.20 Mobile Safari/537.36 OPR/71.3.3718.67322"
	,"Mozilla/5.0 (Linux; U; Android 12; fr-CA; Infinix X676B Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.105 HiBrowser/v2.6.3.1 UWS/ Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.0.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-F711B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; he-IL; Redmi Note 9S Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.133 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.15.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; LE2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.119 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-ES; Mi Note 10 Lite Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.88 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; moto g(50) 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.136 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-SA; Xiaomi 11T Pro Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.90 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn"
	,"Mozilla/5.0 (Linux; Android 12; 2201117PG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.79 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; en-GB; M2101K7AG Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.100 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3"
	,"Mozilla/5.0 (Linux; Android 12; M2012K11AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.114 Mobile Safari/537.36 OPR/71.3.3718.67322"
	,"Mozilla/5.0 (Linux; U; Android 12; es-AR; Mi 10T Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.64 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-A025G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.71 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; CPH2127 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.0 Mobile Safari/537.36 GoogleApp/13.41.11.26.arm64"
	,"Mozilla/5.0 (Linux; U; Android 12; es-EC; CPH2269 Build/JOP24G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.91 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-S906E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.136 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.63 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; V2058 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-EC; POCO M3 Pro 5G Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.105 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.6.0-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; he-IL; POCO X3 NFC Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.133 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.17.0-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; es-US; POCO F4 GT Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.16.3.1-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; es-US; Redmi Note 9 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.56 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-A135F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-M526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5218.213 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A127M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; pt-PT; SM-G975U Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 UCBrowser/13.4.0.1306 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-F721B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4953.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; LM-V500) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.54 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2007J20CI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.103 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A235F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.118 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A127F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.79 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.111 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; ca-ES; Redmi Note 9 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.88 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-A315G Build/SP1A.210812.016; fr-FR) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36 Puffin/9.7.2.51367AP"
	,"Mozilla/5.0 (Linux; Android 12; NE2213) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.79 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; V2046) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.62 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A315G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.167 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; RMX3370) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5113.212 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; Nokia G20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-G970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Mobile Safari/537.36 EdgA/103.0.1264.71"
	,"Mozilla/5.0 (Linux; Android 12; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.123 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; 22021211RG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.75 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; 220733SL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.79 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; ar-EG; Redmi Note 9 Pro Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.160 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.13.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-T227U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; en-US; Xiaomi 12 Lite Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.75 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.18.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.114 Mobile Safari/537.36 OPR/71.3.3718.67322"
	,"Mozilla/5.0 (Linux; Android 12; CPH2269) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.9999.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; CPH2197) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; ar-EG; TECNO CG6j Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.43 HiBrowser/v2.5.7.1 UWS/ Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; RMX3393) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5199.205 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; zh-CN; Redmi Note 10 Pro Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4878.0 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; 22041216G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.121 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-T500) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 OPR/72.0.3767.68191"
	,"Mozilla/5.0 (Linux; Android 12; SM-N986B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.22 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; 21081111RG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.126 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-G781U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.121 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A326U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.98 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-F936W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5113.212 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-T505 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.91 Safari/537.36 OPX/1.6"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-N770F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.134 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; LE2117) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.69 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; vivo 1938 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.122 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/381.0.0.29.105;]"
	,"Mozilla/5.0 (Linux; Android 12; 6102H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-G975U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5227.158 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; moto g(30)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A217M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4844.94 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; CPH2359) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; 2201117TL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.105 Mobile Safari/537.36 OPR/71.3.3718.67322"
	,"Mozilla/5.0 (Linux; Android 12; SM-G975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-N986W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-GQ; Redmi 10 5G Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.90 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.78 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2011K2G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4812.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A125U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/17.0 Chrome/96.0.4664.207 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-S908N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.79 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; moto g 5G (2022)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.125 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A127M Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.79 Mobile Safari/537.36 OPX/1.6"
	,"Mozilla/5.0 (Linux; U; Android 12; ar-EG; SM-G975U Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.87 UCBrowser/13.4.0.1306 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-MX; Redmi Note 10 5G Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.69 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.6.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.125 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A315G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.126 Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-F711B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; Infinix X670) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.170 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; RMX3363) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5113.212 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; de-DE; Mi 11 Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.88 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-A315G Build/SP1A.210812.016; es-VE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36 Puffin/9.7.2.51367AP"
	,"Mozilla/5.0 (Linux; Android 12; SM-A217M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/384.0.0.18.104;]"
	,"Mozilla/5.0 (Linux; U; Android 12; zh-CN; POCO M3 Pro 5G Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.86 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.6.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-N975U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.91 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A217M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; CPH2065) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.62 Mobile Safari/537.36 EdgA/107.0.1418.28"
	,"Mozilla/5.0 (Linux; U; Android 12; es-EC; RMX3085 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.17.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A315G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.164 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; 21091116AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.91 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-G973N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.79 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-G998U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.92 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-F127G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.119 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; TECNO LF7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5218.213 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; en-GB; RMX3085 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.136 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.17.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; CPH2065) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5113.212 Mobile Safari/537.36 OPR/72.3.3767.68685"
	,"Mozilla/5.0 (Linux; U; Android 12; fr-CI; POCO F3 Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5248.169 Mobile Safari/537.36 OPR/71.3.3718.67322"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G973U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.99 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A226B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-N985F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.61 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; Nokia G20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.115 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.9999.0 Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A025M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.69 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; fr-FR; Mi 11 Lite 5G Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.160 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.17.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.79 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-G970U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.168 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; IV2201) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; zh-CN; Xiaomi 11T Pro Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.86 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; es-SA; CPH2043 Build/JOP24G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.106 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; 21121119VL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.105.0.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A127M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5351.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.61 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A215W) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4812.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A336M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.6.96.7 Mobile Safari/537.36 GoogleApp/13.11.10.23.arm64"
	,"Mozilla/5.0 (Linux; Android 12; 220333QL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.115 Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2101K7BL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A715F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.123 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-GQ; Xiaomi 12 Lite Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.88 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.18.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; M2101K7AI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5153.168 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2012K11AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.63 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A035M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.91 Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; zh-CN; Mi 11 Lite 5G Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.162 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.17.0-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; he-IL; TECNO KG5p Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36 PHX/11.0"
	,"Mozilla/5.0 (Linux; Android 12; SM-G975F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.103 Mobile Safari/537.36 OPT/2.9"
	,"Mozilla/5.0 (Linux; Android 12; SM-A325M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.167 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5206.172 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; de-DE; Redmi Note 9 Pro Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.88 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.13.1-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; es-PA; Redmi Note 10 Pro Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.75 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.17.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; M2101K6G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.82 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; 22031116BG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.115 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; V2050) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.115 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; fr-CA; POCO X3 NFC Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4878.0 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.14.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; IN2013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; moto g 5G (2022) Build/S1SAS32.47-59-7; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.15 Mobile Safari/537.36 GoogleApp/13.44.10.26.arm64"
	,"Mozilla/5.0 (Linux; Android 12; SM-A225M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-PA; Mi 10 Lite 5G Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.18.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; 2112123AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5199.205 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2102J20SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; V2110) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; POCO F2 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5113.212 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; Redmi K30) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.112 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; T779W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.124 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; de-DE; Redmi Note 10S Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.60 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.18.0-gn"
	,"Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.79 DuckDuckGo/5 Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; RMX3521) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5113.212 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; en-GB; Redmi Note 10 Pro Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.160 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; M1908C3JGG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.4953.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.58 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; ar-EG; Mi Note 10 Lite Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.88 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; es-MX; 2107113SG Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3"
	,"Mozilla/5.0 (Linux; Android 12; SM-G970F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.71 Mobile Safari/537.36 OPX/1.6"
	,"Mozilla/5.0 (Linux; U; Android 12; es-BO; Redmi Note 10S Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.75 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.15.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; 21091116AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5170.203 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-MX; Redmi Note 11 Build/SKQ1.211103.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.1879 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.14.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; M2102J20SI Build/SQ3A.220705.004) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.125 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-AR; Mi 10T Lite Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4878.0 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.14.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-A225F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5296.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.103 Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; 2201117TG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5180.177 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A225F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5296.0 Mobile Safari/537.36 OPT/2.9"
	,"Mozilla/5.0 (Linux; Android 12; SM-A135U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-MX; POCO X3 NFC Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.60 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.18.0-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; es-SA; Redmi Note 10S Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.75 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.18.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-A516B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.121 Mobile Safari/537.36 EdgA/106.0.1370.52"
	,"Mozilla/5.0 (Linux; U; Android 12; es-VE; Redmi Note 9S Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.64 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.15.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-A725M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-PA; POCO F4 GT Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.114 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.16.3.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; I2018) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5180.177 Mobile Safari/537.36 OPR/72.0.3767.68191"
	,"Mozilla/5.0 (Linux; Android 12; SM-G996U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5113.212 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2003J15SC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.118 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; ar-EG; M2003J15SC Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 UCBrowser/13.4.0.1306 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-EC; RMX3085 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.79 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.17.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-A225M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.122 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2101K7BG Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.115 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; KB2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.168 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A217M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.2 Chrome/83.0.4100.3 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2101K7BL Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.126 Mobile Safari/537.36 OPX/1.6"
	,"Mozilla/5.0 (Linux; Android 12; moto g51 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; AC2001 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.6.96.7 Mobile Safari/537.36 OPX/1.7"
	,"Mozilla/5.0 (Linux; Android 12; SM-A025M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4859.172 Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A135U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.91 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.63 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A315G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4844.88 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; KB2005) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.126 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; fr-CA; Mi 10T Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.79 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-M526BR) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.63 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-M115F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-T505 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.127 Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; zh-CN; CPH2365 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.90 UCBrowser/13.4.0.1306 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; en-GB; TECNO KG5p Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36 PHX/11.0"
	,"Mozilla/5.0 (Linux; U; Android 12; es-MX; POCO X3 Pro Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.60 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.15.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; T671H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.114 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-F916B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5199.205 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; RMX2170) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; Mi 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.87 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5296.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2101K9AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.114 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; CPH2271) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5206.172 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A315G Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.91 Mobile Safari/537.36 OPX/1.6"
	,"Mozilla/5.0 (Linux; Android 12; SM-A725M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A217M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-AR; RMX3085 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.162 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.17.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-A226B Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5206.172 Mobile Safari/537.36 OPX/1.7"
	,"Mozilla/5.0 (Linux; Android 12; motorola edge (2021)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.168 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-BO; Redmi Note 11 Build/SKQ1.211103.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.64 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.14.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-T500) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.71 Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; moto g42) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.106.0.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-ES; TECNO KG5p Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.94 Mobile Safari/537.36 PHX/11.0"
	,"Mozilla/5.0 (Linux; U; Android 12; es-ES; POCO X3 NFC Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.88 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.14.1-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; zh-CN; SM-G975U Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.97 UCBrowser/13.4.0.1306 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; V2139) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.127 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5152.196 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.0 DuckDuckGo/5 Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A125U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4844.51 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-ES; M2102J20SG Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.100 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3"
	,"Mozilla/5.0 (Linux; U; Android 12; es-VE; Mi 11 Lite Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.14.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; RMX2086) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.92 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A326U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.136 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-T220) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4844.51 Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A137F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; he-IL; Mi Note 10 Lite Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4878.0 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; M2101K7AI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5113.212 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; en-GB; Xiaomi 11 Lite 5G NE Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4758.11 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.14.1-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; moto g(30) Build/S0RCS32.41-10-19-6; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.6.96.7 Mobile Safari/537.36 OPR/66.0.2254.63894"
	,"Mozilla/5.0 (Linux; Android 12; 2109119DG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.82 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.119 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; 1eDxhzflyo; U; es) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.110 Mobile Tenta/7.1.0 Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.132 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; ko-KR; Xiaomi 12 Lite Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.79 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.18.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-A125F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.118 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; ar-EG; POCO X3 NFC Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.162 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; es-MX; Redmi Note 9S Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.79 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.14.1-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; es-EC; POCO X3 Pro Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; fr-CA; Mi 10T Lite Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.5.4896.80 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.14.1-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; zh-CN; Mi 11 Lite Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.86 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.12.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; NX709S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.126 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-LA; Xiaomi 11 Lite 5G NE Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.64 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.14.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-A315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5180.177 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A135F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4844.48 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A336M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5199.205 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2101K7BG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.119 Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-F926B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4844.82 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A536E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.126 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2012K11AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.115 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2102J20SG Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.0 Mobile Safari/537.36 OPX/1.6"
	,"Mozilla/5.0 (Linux; Android 12; SM-A135U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.114 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A035M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5199.205 Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; motorola edge 20 Build/S1RGS32.53-18-22-4; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36 EdgW/1.0"
	,"Mozilla/5.0 (Linux; Android 12; SM-A217M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; TNA-AN00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-US; Redmi 10 5G Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.90 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-A315G Build/SP1A.210812.016; en-US) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Mobile Safari/537.36 Puffin/9.7.2.51367AP"
	,"Mozilla/5.0 (Linux; Android 12; nKOGZZggEs; U; es) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.15 Mobile AvastSecureBrowser/7.1.1 Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; he-IL; Infinix X670 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.70 UCBrowser/13.4.0.1306 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A725M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.75 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A225M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.105.0.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; ko-KR; Mi 10T Lite Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.5.4896.80 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.14.1-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; SM-A525M Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5153.168 Mobile Safari/537.36 OPR/65.0.2254.63211"
	,"Mozilla/5.0 (Linux; Android 12; SM-N975U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.115 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; 2201117TL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A226BR) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 Mobile Safari/537.36 OPR/69.3.3606.65458"
	,"Mozilla/5.0 (Linux; Android 12; SM-N981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.54 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.115 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; CPH2333) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.168 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A315G Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.0.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-PA; Mi 10 Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-G781U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-GQ; POCO M3 Pro 5G Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.86 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.6.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; M2101K7AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.6.96.7 Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-G996U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5180.177 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; FNE-NX9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4859.172 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; de-DE; Mi 11 Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; CPH2371) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.103 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; zh-CN; POCO X3 NFC Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4758.11 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.18.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; CPH2363) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5227.158 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2102J20SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.94 Mobile Safari/537.36 OPR/68.3.3557.64528"
	,"Mozilla/5.0 (Linux; Android 12; M2011K2G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5248.169 Mobile Safari/537.36 OPR/71.3.3718.67322"
	,"Mozilla/5.0 (Linux; Android 12; SM-T220) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.1879 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; en-US; Mi 10 Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.128 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; en-GB; POCO X3 NFC Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.14.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-A115M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5296.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A515F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.168 Mobile Safari/537.36 OPX/1.7"
	,"Mozilla/5.0 (Linux; U; Android 12; es-US; Redmi Note 10S Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.75 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.15.0-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; zh-CN; POCO F3 Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.1879 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.0-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; es-US; Redmi Note 10 Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.90 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.11.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-S908U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5296.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A516U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.110 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-PA; Redmi Note 9 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.133 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-N986U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.105.0.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2007J3SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.170 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-G985F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; CPH2359 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5296.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; moto g(50)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A127M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-EC; POCO F3 Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.79 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.0-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; pt-PT; Redmi Note 10 Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.79 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.14.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-A725M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.114 Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2101K6R) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.119 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-N975W) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.75 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; moto e32(s)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.105 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.94 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A217M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.98 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-MX; Redmi Note 10 Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.14.1-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; ko-KR; Redmi Note 9S Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; es-SA; POCO X3 NFC Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.133 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.17.0-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; es-VE; Infinix X676B Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.159 HiBrowser/v2.6.3.1 UWS/ Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-N980F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.92 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-EC; TECNO KG5p Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.48 Mobile Safari/537.36 PHX/11.0"
	,"Mozilla/5.0 (Linux; Android 12; V2066) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; vivo 1935) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.34 Mobile Safari/537.36 OPR/71.3.3718.67322"
	,"Mozilla/5.0 (Linux; U; Android 12; de-DE; POCO X3 NFC Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.1879 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-A908N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5152.196 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-US; Redmi Note 9S Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.160 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.15.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-A135M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; tbS8rchbTR; U; es) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5206.172 Mobile Tenta/7.1.0 Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.87 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A127M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.65 Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A037U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2101K7BG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A125U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.115 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; arm_64; Android 12; SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.101 YaBrowser/22.9.8.37.00 SA/3 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-BO; Mi 11 Lite 5G Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.60 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.17.0-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; es-LA; POCO X3 Pro Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; en-US; M2102J20SG Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.79 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A217F/A217FXXU8DVG4) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4844.84 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.119 Mobile Safari/537.36 OPR/72.3.3767.68685"
	,"Mozilla/5.0 (Linux; Android 12; SM-A715F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.9999.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; ca-ES; SM-A217M Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.87 UCBrowser/13.4.0.1306 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G991N) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4844.84 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; en-GB; POCO X3 NFC Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.133 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; 2201117TG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.104 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-PA; Redmi Note 9S Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.14.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A325M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.63 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-S908E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5199.205 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-G970U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.127 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-G780F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5113.212 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A225M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.26 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; V2118) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.78 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2101K6R) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-G998U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4079.50 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A127M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4844.94 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2101K7BNY) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.62 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A226BR) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-SA; Redmi 10 5G Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn"
	,"Mozilla/5.0 (Linux; Android 12; ASUS_I006D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.92 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2101K6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-VE; Mi 11 Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4878.0 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; fr-CA; Redmi Note 9S Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.133 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.14.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A336B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4844.51 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; 2201117TG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.105 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; 21061119AL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.79 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A025M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.70 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; en-US; SM-G975U Build/SP1A.210812.016) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.2 UCBrowser/13.4.2.1306 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30"
	,"Mozilla/5.0 (Linux; Android 12; CPH2359 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.107 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; en-US; Mi Note 10 Lite Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4758.11 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; LE2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-VE; POCO X3 Pro Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.133 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.15.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-G781B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A426B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.62 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-N986U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; V2109) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; en-GB; Infinix X670 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.70 UCBrowser/13.4.0.1306 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; de-DE; Infinix X670 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.43 HiBrowser/v2.6.3.1 UWS/ Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; IN2017) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5152.196 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; en-GB; POCO X3 Pro Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; es-SA; Xiaomi 12 Lite Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.1879 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.18.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-N970U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.79 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; de-DE; Redmi Note 10S Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.133 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.18.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-A225F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.110 Mobile Safari/537.36 OPT/2.9"
	,"Mozilla/5.0 (Linux; Android 12; V2202) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2102J20SG Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.87 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.114 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; tbS8rchbTR; U; es) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5296.0 Mobile Tenta/7.1.0 Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2101K6R Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5152.196 Mobile Safari/537.36 OPX/1.6"
	,"Mozilla/5.0 (Linux; Android 12; SM-S906E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.91 Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G991B/G991BXXS5CVIF) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4812.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; ar-EG; Mi Note 10 Lite Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.133 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; he-IL; Redmi Note 10 Pro Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.5.4896.80 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.17.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-A217M Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.170 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G975U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.62 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2101K7BL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.87 Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; RMX3151) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.62 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2101K6R Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.127 Mobile Safari/537.36 OPT/2.9"
	,"Mozilla/5.0 (Linux; U; Android 12; fr-FR; TECNO KG5p Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36 PHX/11.0"
	,"Mozilla/5.0 (Linux; Android 12; M2101K7AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.118 Mobile Safari/537.36 OPR/72.1.3767.68311"
	,"Mozilla/5.0 (Linux; U; Android 12; es-MX; Redmi Note 9S Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.64 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; 21081111RG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-G981V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.136 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SHARK PAR-H0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.118 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-N975F/N975FXXU8HVH8) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.77.34.5 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A225F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.110 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-PA; Redmi Note 10S Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.162 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.15.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-A127M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.164 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-VE; RMX3085 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.75 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.17.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-T505) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.112 Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2102J20SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A127F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5180.177 Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; ca-ES; POCO X3 NFC Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.1879 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.17.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; M2012K11G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.112 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; ca-ES; TECNO KG5p Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.77.34.5 Mobile Safari/537.36 PHX/11.0"
	,"Mozilla/5.0 (Linux; Android 12; V2110) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.79 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; ar-EG; M2102J20SG Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.62 UCBrowser/13.4.0.1306 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-EC; Redmi Note 10S Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.56 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.15.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; M2012K11AG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.65 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; CPH2365) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; 21121119SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.112 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A536E) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4079.50 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-US; Mi 11 Lite 5G Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.64 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.17.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-A315G Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5199.205 Mobile Safari/537.36 OPX/1.7"
	,"Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile DuckDuckGo/5 Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A415F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.126 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-F916B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4844.48 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; CPH2273) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.70 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-US; Redmi Note 9 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.64 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; M2102J20SI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.63 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; RMX3191) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5296.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A336E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.62 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; ar-EG; POCO X3 NFC Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.18.0-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; es-LA; Mi 10T Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.56 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; TECNO LF7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; ar-EG; TECNO CG6j Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.105 HiBrowser/v2.5.7.1 UWS/ Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-US; RMX3085 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4758.11 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.17.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5142.217 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-G973U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; he-IL; M2003J15SC Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 UCBrowser/13.4.0.1306 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; moto g(50) 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.69 Mobile Safari/537.36 OPR/71.3.3718.67322"
	,"Mozilla/5.0 (Linux; Android 12; SM-S908E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.98 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2012K11G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5206.172 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A217M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.0 Chrome/87.0.3945.79 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; fr-CI; M2102J20SG Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.4.0.1306 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A025M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.112 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A226B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.121 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; 220333QNY) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5238.167 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2007J17G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.4953.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; en-US; Redmi Note 9S Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4878.0 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.15.0-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; zh-CN; Redmi Note 9 Pro Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.5.4896.80 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.13.1-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; en-US; Mi Note 10 Lite Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.82 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; V2046) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4844.84 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; Redmi Note 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.54 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; 2107113SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.92 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-M025F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.122 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-M115M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.79 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-EC; RMX3085 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.1879 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.17.0-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; 2201117TG Build/SKQ1.211103.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.112 Mobile Safari/537.36 OPR/65.2.2254.63594"
	,"Mozilla/5.0 (Linux; Android 12; SM-A325F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.77.34.5 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A325M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5206.172 Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; 21091116UG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4859.172 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; RMX3472) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.70 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; DE2118) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.91 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.91 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; XQ-AU51) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5152.196 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A908N) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.75 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-GQ; Mi 10T Lite Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.136 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.14.1-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; es-ES; Redmi Note 10 Pro Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.17.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.125 Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; ar-EG; Redmi Note 10 Pro Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; RMX3472) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.1899.105 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; 2201117PG Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.6.96.7 Mobile Safari/537.36 OPX/1.7"
	,"Mozilla/5.0 (Linux; Android 12; SM-A526U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.105 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-ES; POCO X3 Pro Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4878.0 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.15.0-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; pt-PT; Xiaomi 11T Pro Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.82 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-S134DL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.129 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; ar-EG; Mi 11 Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.86 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.10.0-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; ar-EG; TECNO KG5p Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Mobile Safari/537.36 PHX/11.0"
	,"Mozilla/5.0 (Linux; Android 12; 2201117TG Build/SKQ1.211103.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.91 Mobile Safari/537.36 OPX/1.6"
	,"Mozilla/5.0 (Linux; Android 12; SM-N986B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.91 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SCG08) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.15 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-G780F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.9999.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-G970F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.79 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S908E) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.63 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; pt-PT; SM-G975U Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.4.0.1306 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-BO; Mi 10 Lite 5G Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.56 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.18.0-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; ko-KR; CPH2365 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.70 UCBrowser/13.4.0.1306 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; CPH2173) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.104 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-US; Infinix X676B Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.101 HiBrowser/v2.6.3.1 UWS/ Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2101K6R) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.124 Mobile Safari/537.36 OPR/71.3.3718.67322"
	,"Mozilla/5.0 (Linux; U; Android 12; he-IL; TECNO KG5p Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4812.0 Mobile Safari/537.36 PHX/11.0"
	,"Mozilla/5.0 (Linux; Android 12; M2101K6G Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.87 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-S908E) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.167 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; en-GB; POCO X3 Pro Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.162 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.14.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; moto g(100)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.92 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; he-IL; POCO X3 NFC Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-A025G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; moto g(50) 5G Build/S1RSS32.38-20-7-5; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5152.196 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A528B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5351.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; CPH2195) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5142.217 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2103K19G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.123 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A226BR Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.110 Mobile Safari/537.36 OPX/1.7"
	,"Mozilla/5.0 (Linux; Android 12; RMX2086) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.115 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2007J3SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.121 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; de-DE; Redmi Note 10 Pro Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.75 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-A225M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.20 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-T735) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.170 Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; TECNO KH6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.114 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; RMX3151) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.127 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A217M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5199.205 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M1908C3JGG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.92 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; he-IL; Mi 10 Lite 5G Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.1879 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.18.0-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; fr-FR; POCO X3 NFC Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.64 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.18.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; ASUS_I005DA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.15 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A115M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.1899.105 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; LE2127) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.112 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-F936B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.110 Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5199.205 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-VE; RMX3085 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.1879 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.17.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-T505N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.126 Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; V2057) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A326U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5180.177 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; XQ-AU51) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.79 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.78 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-G780F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-N975U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4844.58 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2101K7BL Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.107 Mobile Safari/537.36 GoogleApp/13.43.18.26.arm64"
	,"Mozilla/5.0 (Linux; Android 12; CPH2363) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-MX; Mi 10 Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.114 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn"
	,"Mozilla/5.0 (Linux; Android 12; M2007J17G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.62 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-LA; SM-G975U Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.87 UCBrowser/13.4.0.1306 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; motorola edge 30) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G975U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.9999.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2102K1G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5180.177 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; fr-FR; Mi 10T Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.162 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; LM-G820) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.91 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-S215DL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5238.167 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-S515DL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.112 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A035M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5199.205 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-MX; Redmi Note 9S Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.14.0-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; he-IL; Redmi Note 10S Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.64 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.15.0-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; fr-CA; Redmi Note 9 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.82 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; es-EC; Redmi Note 9S Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.133 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.15.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-G996U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.92 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; ca-ES; Xiaomi Pad 5 Build/SKQ1.220303.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.86 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.6.0-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; ar-EG; POCO X3 Pro Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.79 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.14.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-G988N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.118 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-MX; TECNO KG5p Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36 PHX/11.0"
	,"Mozilla/5.0 (Linux; Android 12; SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A215U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.2 Chrome/92.0.0.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; V2109) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.20 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; fr-CA; POCO X3 Pro Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4878.0 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.15.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; M2103K19Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-S906E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.118 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2003J15SC Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.0.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; ca-ES; POCO X3 Pro Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.60 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.14.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-T505) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5153.168 Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-MX; POCO X3 Pro Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.75 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.14.1-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; es-ES; POCO F3 Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; XQ-AU51) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.91 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; en-GB; POCO X3 Pro Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.136 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.15.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; vivo 1935) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.162 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-AR; Redmi Note 9S Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.60 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.14.0-gn"
	,"Mozilla/5.0 (Linux; arm_64; Android 12; SM-A525M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.170 YaBrowser/22.11.1.75.00 SA/3 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-G975U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5296.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; he-IL; Redmi Note 9 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.88 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; zh-CN; CPH2365 Build/RKQ1.211119.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 UCBrowser/13.4.0.1306 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; 2201117TG Build/SKQ1.211103.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.118 Mobile Safari/537.36 OPR/65.2.2254.63594"
	,"Mozilla/5.0 (Linux; U; Android 12; es-GQ; M2102J20SG Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36 XiaoMi/Mint Browser/3.9.3"
	,"Mozilla/5.0 (Linux; Android 12; V2110) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.109 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-G9860) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.115 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A225M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4859.172 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A037F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.34 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-S127DL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.119 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; RMX3081) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.92 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; fr-CA; Redmi Note 9 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.160 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; fr-CI; Redmi Note 9S Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.79 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.14.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G970F/G970FXXUGHVJ5) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.134 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; ar-EG; Redmi Note 10 Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.136 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.14.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A235M Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-BO; SM-A315G Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.90 UCBrowser/13.4.0.1306 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-VE; Redmi Note 10 Pro Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.105 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; es-MX; POCO X3 NFC Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.64 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.18.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; M2102J20SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.92 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A526U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.121 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-LA; Redmi Note 10 Pro Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; es-VE; Mi 11 Lite 5G Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.17.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; RMX3081) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.101 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A135M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2003J15SC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; LM-V500) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5296.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2101K7BG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.114 Mobile Safari/537.36 OPR/72.3.3767.68685"
	,"Mozilla/5.0 (Linux; Android 12; motorola edge (2021)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.115 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; moto e22i) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A326U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4844.84 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; pt-PT; Mi 11 Lite Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.1879 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.14.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; CPH2195) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.105 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A525F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.105 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; CPH2205) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.104 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2101K6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.15 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.110 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; CPH2217) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; vivo 1938) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.15 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; TECNO CI8n) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.121 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-ES; Redmi Note 9 Pro Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.82 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.13.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; DE2117) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.105 Mobile Safari/537.36"
	,"Mozilla/5.0 (Android 12; Mobile; rv:107.0) Gecko/107.0 Firefox/107.0"
	,"Mozilla/5.0 (Linux; Android 12; U616AT Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.124 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-EC; Redmi Note 10 Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.56 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.14.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-P610 Build/SP2A.220305.013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.6.96.7 Safari/537.36 OPX/1.7"
	,"Mozilla/5.0 (Linux; Android 12; Nokia G20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.88 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; Infinix X6819) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-US; Redmi Note 11 Build/SKQ1.211103.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.160 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.14.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; XQ-CC54) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2101K6P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.105 Mobile Safari/537.36"
	,"Mozilla/5.0 (Android 12; Mobile; rv:100.0) Gecko/100.0 Firefox/100.0"
	,"Mozilla/5.0 (Linux; Android 12; M2012K10C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.70 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A315G Build/SP1A.210812.016; es-EC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0 Mobile Safari/537.36 Puffin/9.7.2.51367AP"
	,"Mozilla/5.0 (Linux; Android 12; SM-F711U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5113.212 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; Nokia G50) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.105 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-G770F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5113.212 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-M135M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4812.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; en-GB; Mi 11 Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.72 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.10.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; Infinix X6817) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.125 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; CPH2065) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; CPH2065) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.34 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2101K9G Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36 OPX/1.7"
	,"Mozilla/5.0 (Linux; U; Android 12; es-EC; TECNO CG6j Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.157 HiBrowser/v2.5.7.1 UWS/ Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-ES; Mi 11 Lite 5G Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.133 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.17.0-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; fr-CA; Redmi Note 10S Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.60 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.18.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G996B/G996BXXS5CVIF) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.0.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-G981U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.170 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-S901U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5180.177 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-F936W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.118 Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; en-GB; Mi 10 Lite 5G Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4878.0 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.18.0-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; ko-KR; Mi 11 Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.90 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.10.0-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; pt-PT; Xiaomi Pad 5 Build/SKQ1.220303.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.128 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.6.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-A315G Build/SP1A.210812.016; ar-EG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36 Puffin/9.7.2.51367AP"
	,"Mozilla/5.0 (Linux; U; Android 12; fr-CA; Redmi Note 10 Pro Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.128 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.18.3-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-T505) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.54 Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G975U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.98 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; en-GB; POCO X3 NFC Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.88 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; zh-CN; Mi 11 Lite 5G Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.136 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.17.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; ASUS_I003DD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.6.96.7 Mobile Safari/537.36 EdgA/107.0.1418.28"
	,"Mozilla/5.0 (Linux; Android 12; V2053) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.54 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; RMX3081) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.105 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A135M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.136 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-T875) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5113.212 Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.6.96.7 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-VE; Redmi Note 9S Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.136 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; ca-ES; Redmi Note 9 Pro Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.13.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; vivo 1935) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.103 Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; motorola edge 20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5180.177 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; ca-ES; POCO X3 NFC Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.60 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; es-AR; Mi Note 10 Lite Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.75 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; ASUS_I006D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5238.167 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; 2201117TL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5113.212 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A336B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5238.167 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; fr-FR; POCO F3 Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4878.0 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.0-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; es-PA; POCO X3 NFC Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4878.0 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.18.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; moto g(30)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Mobile Safari/537.36 (Ecosia android@101.0.4951.41)"
	,"Mozilla/5.0 (Linux; U; Android 12; es-VE; Mi Note 10 Lite Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.88 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; U; Android 12; es-GQ; POCO X3 NFC Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.5.4896.80 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-M135M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4844.84 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; en-US; Redmi Note 11 Build/SKQ1.211103.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.90 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.6.0-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-A325M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.1899.105 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; V2050) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.91 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A225M Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.107 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-LA; POCO X3 NFC Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.14.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; SM-M515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.148 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; M2101K6I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.5.4896.80 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-M325FV) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4844.74 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; es-SA; Redmi Note 9S Build/SKQ1.211019.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.160 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.16.1-gn"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5206.172 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; Nokia X20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.170 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-T735) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.126 Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A235M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4512.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G991U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4079.50 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4844.48 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G998B/G998BXXS5CVIF) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4812.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A135F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.9999.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; SM-A035G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.63 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; Android 12; CPH2161) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
	,"Mozilla/5.0 (Linux; U; Android 12; zh-CN; Redmi Note 10 5G Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.90 Mobile Safari/537.36 XiaoMi/MiuiBrowser/13.6.0-gn"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1 OPT/3.3.9"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0.3 Mobile/15E148 DuckDuckGo/7 Safari/605.1.15"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0.2 Mobile/15E148 Safari/604.1 OPT/3.3.8"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/107.0.5304.101 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1 OPX/1.6.2"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/106.0.5249.70 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/96.0.4664.53 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Version/16.0.2 Safari/605.1.15 AlohaBrowser/4.3.0"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Version/16.1 Safari/605.1.15 AlohaBrowser/4.3.0"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/236.0.484392333 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Snapchat/12.01.1.24 (like Safari/8614.1.25.0.30, panda)"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0.3 Mobile/15E148 DuckDuckGo/7 Safari/605.1.15"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Mobile/15E148 DuckDuckGo/7 Safari/605.1.15"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/1.0.7.0 Mobile/15E148 Safari/605.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/233.0.478398274 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/233.0.478398274 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/216.0.453113025 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/211.1.447770393 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Version/16.0.2 Safari/605.1.15 AlohaBrowser/4.3.0"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/236.0.484392333 Mobile/20A380 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) AvastSecureBrowser/4.9.0 Mobile/15E148 Version/16.2 Safari/605.1.15"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0.3 Mobile/15E148 Safari/605.1.15/4604591328"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/234.0.480739195 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Version/16.0.3 Safari/605.1.15 AlohaBrowser/4.3.0"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.163 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0.3 Mobile/15E148 Safari/604.1 OPT/3.3.10"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) EdgiOS/106.0.1370.47 Version/16.0.2 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/96.0.4664.116 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0.3 Mobile/15E148 Snapchat/12.07.0.32 (like Safari/8614.1.25.0.30, panda)"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Mobile/15E148 Safari/604.1 OPX/1.7.0"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1 OPT/3.3.8"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/105.0.5195.147 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/99.0.4844.47 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Mobile/15E148 Safari/604.1 OPX/1.7.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/104 Mobile/15E148 Safari/605.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/605.1.15/4604591328"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0.2 YaBrowser/22.9.6.529.10 SA/3 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/99.0.4844.59 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0.2 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/90.0.4430.216 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/231.0.475926209 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/86.0.4240.77 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/99.0.4844.47 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 YaBrowser/22.9.6.529.10 SA/3 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.3 Mobile/15E148 DuckDuckGo/7 Safari/605.1.15"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.7 Mobile/15E148 Safari/605.1.15/4418203472"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/104.0.5112.88 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/106.0.5249.75 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4,2 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/100.0.4896.56 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Mobile/15E148 Safari/604.1 RDDocuments/8.2.4.887"
	,"Mozilla/5.0 (iPod touch; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.3 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Snapchat/12.01.1.24 (like Safari/8613.2.7.0.7, panda)"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.3 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) EdgiOS/106.0.1370.52 Version/15.6 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/235.0.482074324 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/223.0.463913120 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1 OPX/1.6.2"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/81.0.4044.124 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/230.1.475637890 Mobile/19F77 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/107.0.5304.101 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/105.0.5195.100 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/105.0.5195.147 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/605.1.15/4354416112"
	,"Mozilla/5.0 (iPod touch; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.7 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/232.0.476785961 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/105.0.5195.129 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/107.0.5304.101 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.3 Mobile/15E148 Safari/604.1 OPT/3.3.9"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Mobile/15E148 Safari/604.1 OPX/1.6.2"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.3 Mobile/15E148 Safari/604.1 OPX/1.6.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/104.0.5112.99 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Mobile/15E148 Safari/605.1.15/4418203472"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Mobile/15E148 Safari/605.1.15/4418203472"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Mobile/15E148 Safari/604.1 OPX/1.7.0"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.7 Mobile/15E148 Safari/605.1.15"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/105.0.5195.69 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1 OPT/3.3.9"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Mobile/15E148 Snapchat/12.05.0.12 (like Safari/8613.3.9.0.16, panda)"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.7 Mobile/15E148 Safari/604.1 OPX/1.6.2"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/103.0.5060.63 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/605.1.15/4418203472"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Mobile/15E148 DuckDuckGo/7 Safari/605.1.15"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.3 Mobile/15E148 Safari/604.1 (compatible; YandexMobileBot/3.0;  http://yandex.com/bots)"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/231.0.475926209 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Mobile/15E148 DuckDuckGo/7 Safari/605.1.15"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/101.0.4951.58 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Mobile/15E148 DuckDuckGo/7 Safari/605.1.15"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Mobile/15E148 Safari/605.1.15"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) EdgiOS/105.0.1343.47 Version/15.4 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/105.0.5195.69 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/104.0.5112.99 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/225.0.466661455 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/236.0.484392333 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 DuckDuckGo/7 Safari/605.1.15"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/233.0.478398274 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Mobile/15E148 Safari/604.1 OPX/1.7.0"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/107.0.5304.101 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.3 Mobile/15E148 Safari/605.1.15/4410339824"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Mobile/15E148 DuckDuckGo/7 Safari/605.1.15"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.7 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/228.0.471065565 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Mobile/15E148 Safari/604.1 (compatible; YandexMobileBot/3.0; +http://yandex.com/bots)"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/104.0.5112.88 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/605.1.15"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/218.0.456502374 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/215.1.452881003 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3,2 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/174.1.391956124 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/105.0.5195.98 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/123.4.330040034 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/238.1.487893381 Mobile/19H12 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/236.0.484392333 Mobile/19F77 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1 (compatible; YandexMobileBot/3.0;  http://yandex.com/bots)"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Mobile/15E148 Snapchat/12.01.1.24 (like Safari/8613.2.7.0.7, panda)"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/105.0.5195.37 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/223.0.463913120 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/106.0.5249.126 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/106.0.5249.92 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/227.1.470269224 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/206.1.438432329 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/107.0.5304.66 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/105.0.5195.129 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.3 Mobile/15E148 Safari/604.1 OPX/1.7.0"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/103.0.5060.63 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/605.1.15/4836077776"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/101.0.4951.44 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/105.0.5195.100 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/155.0.367387567 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1 OPT/3.3.8"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/106.0.5249.126 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.8 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/106.0.5249.75 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/210.0.444145502 Mobile/18H17 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/107.0.5304.101 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.3 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Snapchat/12.05.0.12 (like Safari/604.1, panda)"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/107.0.5304.66 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/233.0.478398274 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/175.0.393249130 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_0_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.3 Mobile/15E148 Safari/604.1 OPT/3.3.8"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/227.1.470269224 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.8 Mobile/15E148 Safari/604.1 OPT/3.3.8"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/101.0.4951.58 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/105.0.5195.100 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/107.0.5304.101 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/105.0.5195.69 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/106.0.5249.60 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/103.0.5060.63 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/236.0.484392333 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/105.0.5195.69 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.4 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/235.0.482074324 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/93.0.4577.78 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 YaBrowser/22.11.0.2001.10 SA/3 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Mobile/15E148 Safari/605.1.15"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/106.0.5249.60 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) GSA/234.1.481780343 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/105.0.5195.98 Mobile/15E148 Safari/604.1"
	,"Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/104.0.5112.99 Mobile/15E148 Safari/604.1"
	]

	return list[random.randint(0,len(list)-1)]

mobile_agent = get_mobile_agent()

def chromeWebdriver():
	if Type == "server" :
		chrome_service = ChromeService(ChromeDriverManager(version="114.0.5735.90").install())
		chrome_options = uc.ChromeOptions()


		chrome_options.add_argument('--headless=new')
		chrome_options.add_argument('--no-sandbox')
		chrome_options.add_argument('--blink-settings=imagesEnabled=false')
		chrome_options.add_argument('--window-size=1920,1080')
		chrome_options.add_argument('--disable-dev-shm-usage')
		chrome_options.add_argument('--disable-blink-features=AutomationControlled')
		chrome_options.add_argument('--disable-infobars')
		chrome_options.add_argument('--disable-setuid-sandbox')
		chrome_options.add_argument('--disable-gpu')    
		chrome_options.add_argument('--user-agent=' + mobile_agent)

		chrome_options.page_load_strategy = 'normal'
		driver = uc.Chrome(service=chrome_service, options=chrome_options, version_main=114)
	else :
		chrome_service = ChromeService(executable_path=ChromeDriverManager(version="114.0.5735.90").install())
		chrome_options = Options()
		chrome_options.add_experimental_option('detach', True)
		chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
		if Type == "pc" :
			chrome_options.add_argument('--headless')
		chrome_options.add_argument('--no-sandbox')

		#chrome_options.add_argument("window-size=1920,1080")
		chrome_options.add_argument('user-agent='+ mobile_agent)

		driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

	return driver
	
MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)

Type = MConfig['Type']
SelectHref = MConfig['SelectHref']
Search1 = MConfig['Search1']
Search2 = MConfig['Search2']
Search3 = MConfig['Search3']

if SelectHref == "n" :
	print('error')
	exit()

search1 = ''
search2 = ''
search3 = ''

if Search1 != "n" :
	search1 = Search1[random.randint(0,len(Search1)-1)]
if Search2 != "n" :
	search2 = Search2[random.randint(0,len(Search2)-1)]
if Search3 != "n" :
	search3 = Search3[random.randint(0,len(Search3)-1)]
	
driver = chromeWebdriver()
driver.delete_all_cookies()
SiteUrl = "https://m.naver.com"
driver.get(SiteUrl)
driver.implicitly_wait(10) # 처음에만 셋팅
time.sleep(random.randint(2, 5))


# 검색창 클릭

# 모바일인 경우
driver.find_element(By.XPATH, '//*[@id="MM_SEARCH_FAKE"]').click()

elem = driver.find_element(By.XPATH, '//*[@id="query"]')
time.sleep(random.randint(2, 7))

for val in list(search1) :
	elem.send_keys(str(val))
	time.sleep(random.uniform(0.1, 2))

elem.send_keys(Keys.ENTER)
time.sleep(random.randint(2, 7))

mecotine_chk = 'n'

try :
	e = driver.find_elements(By.CSS_SELECTOR, "a[href='"+str(SelectHref)+"']")
	if e :
		mecotine_chk = 'y'
	else :
		try :
			driver.find_element(By.XPATH, '//*[@class="api_more"]').click()
			time.sleep(random.randint(2, 7))
			e = driver.find_elements(By.CSS_SELECTOR, "a[href='"+str(SelectHref)+"']")
			if e :
				mecotine_chk = 'y'
			else :
				driver.execute_script("window.history.go(-1)")
		except :
			print("EXCEPT1")	
except :
	print("EXCEPT2")

if mecotine_chk == "n" and search2 != "n" :
	time.sleep(random.randint(2, 4))
	driver.find_element(By.XPATH, '//*[@id="nx_query"]').click()
	elem = driver.find_element(By.XPATH, '//*[@id="nx_query"]')
	if search1 == search2 :
		elem.clear()
	else :
		elem.send_keys(" ")
	for val2 in list(search2) :
		elem.send_keys(str(val2))
		time.sleep(random.uniform(0.1, 2))

	elem.send_keys(Keys.ENTER)
	time.sleep(random.randint(2, 7))

	try :
		e = driver.find_elements(By.CSS_SELECTOR, "a[href='"+str(SelectHref)+"']")
		if e :
			mecotine_chk = 'y'
		else :
			try :
				driver.find_element(By.XPATH, '//*[@class="api_more"]').click()
				time.sleep(random.randint(2, 7))
				e = driver.find_elements(By.CSS_SELECTOR, "a[href='"+str(SelectHref)+"']")
				if e :
					mecotine_chk = 'y'
				else :
					driver.execute_script("window.history.go(-1)")
			except :
				print("EXCEPT3")	
	except :
		print("EXCEPT4")

if mecotine_chk == "n" and search3 != "n" :
	time.sleep(random.randint(2, 4))
	driver.find_element(By.XPATH, '//*[@id="nx_query"]').click()
	elem = driver.find_element(By.XPATH, '//*[@id="nx_query"]')
	
	elem.clear()
	time.sleep(random.randint(1, 2))
	for val3 in list(search3) :
		elem.send_keys(str(val3))
		time.sleep(random.uniform(0.1, 2))
	elem.send_keys(Keys.ENTER)
	time.sleep(random.randint(2, 7))

	try :
		e = driver.find_elements(By.CSS_SELECTOR, "a[href='"+str(SelectHref)+"']")
		if e :
			mecotine_chk = 'y'
		else :
			try :
				driver.find_element(By.XPATH, '//*[@class="api_more"]').click()
				time.sleep(random.randint(2, 7))
				e = driver.find_elements(By.CSS_SELECTOR, "a[href='"+str(SelectHref)+"']")
				if e :
					mecotine_chk = 'y'
			except :
				print("EXCEPT5")			
	except :
		print("EXCEPT6")

if mecotine_chk == "y" :
	try:

		time.sleep(random.randint(2, 7))

		e[0].click()
			
		time.sleep(random.randint(20, 46))

		a_elements = driver.find_elements(By.CSS_SELECTOR, ".main_disp a[href*='shopdetail']")

		a_elements[random.randint(0, len(a_elements)-1)].click()

		time.sleep(random.randint(20, 55))

		driver.execute_script("window.history.go(-1)")

		time.sleep(random.randint(5, 12))

		print("SUCCESS")

	except:
		print("EXCEPT7")



driver.quit()


if Type == "pc" :
	_Dir_ = "C:/_Ntos_"

	Rand_hours = random.randint(5,10)
	Rand_minutes = random.randint(1,59)
	sName = "_mitem"
	sSchedule = datetime.datetime.now() + datetime.timedelta(hours=Rand_hours, minutes=Rand_minutes)

	os.system('schtasks /delete /tn '+ sName +' /f')
	time.sleep(1)

	os.system('schtasks /create /tn '+ sName +' /tr '+ _Dir_ +'/mitem.bat /sc once /st '+ sSchedule.strftime('%H:%M') +' /sd '+ sSchedule.strftime('%Y/%m/%d'))
