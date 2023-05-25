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
MConfig = json.loads(MConfigData)

IslId_SiteUrl = MConfig['IslId_SiteUrl']
CustId = MConfig['CustId']

FileSendSave = MConfig['FileSendSave']  #저장후 전송여부
NtosServer = MConfig['NtosServer']  #전송서버 url

FileDir = MConfig['FileDir']  #저장폴더
UserAgent = MConfig['UserAgent']

TotMsg = ''
for val in IslId_SiteUrl :
	#저장html
	SaveHtml = ''
	#에러msg
	ErrMsg = ''
	(SiteUrl, SaveFileName) = val.split("|@|")
	OriginUrl = "<ntosoriginurl>"+str(SiteUrl)+"</ntosoriginurl>\n\n"
	#저장파일명
	SaveFile = FileDir+str(SaveFileName)
	SaveFile = SaveFile.replace('.html', '_'+str(time.strftime('%H%M', time.localtime(time.time())))+'.html')
  
	if SiteUrl == "" or SaveFileName == "" :
		continue
	print(SiteUrl+"<br>")
	try :
		PageHtml = requests.get(SiteUrl)
		PageHtml = PageHtml.text
		PageHtmlRecode = PageHtml.status_code
	except :
		PageHtml = ''
		PageHtmlRecode = 'error'
		ErrMsg = ErrMsg + str(traceback.format_exc()) + "\n\n"
