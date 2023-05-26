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
import re

#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

IslId_SiteUrl = []

MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)

IslId_SiteUrl = MConfig['IslId_SiteUrl']
CustId = MConfig['CustId']

FileSendSave = MConfig['FileSendSave']  #저장후 전송여부
NtosServer = MConfig['NtosServer']  #전송서버 url

FileDir = MConfig['FileDir']  #저장폴더


for val in IslId_SiteUrl :
	#저장html
	SaveHtml = ''
	#에러msg
	ErrMsg = ''
	#상세설명
	DetailHtml = ''
	#상품정보
	PageHtmlJsonData = ''
	#상품정보 Json
	PageHtmlJson = ''
	(SiteUrl, SaveFileName) = val.split("|@|")
	print(SiteUrl)
