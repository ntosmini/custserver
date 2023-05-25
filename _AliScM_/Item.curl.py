# -*- coding: utf-8 -*- 
#알리 상품 모바일 curl

import time
import sys
import json
import io
import os
import random
import requests
import traceback

#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

IslId_SiteUrl = []

MConfigData = sys.argv[1]
try :
	MConfig = json.loads(MConfigData)
	err = 'ok'
except :
	err = "<br><br>"+traceback.format_exc()
print(str(err))

