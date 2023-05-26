# -*- coding: utf-8 -*- 
# 테스트 curl

import time
import sys
import json
import io
import os
import requests
import traceback

MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)

SiteUrl = MConfig['SiteUrl']

PageHtml = requests.get(SiteUrl)
print(PageHtml)
