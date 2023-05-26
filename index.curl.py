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
UserAgent = MConfig['UserAgent']
headers = {
	"User-Agent":UserAgent
}

PageHtml = requests.get(SiteUrl, headers=headers)
PageHtml = PageHtml.text
print(PageHtml)
