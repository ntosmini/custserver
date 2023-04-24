# -*- coding: utf-8 -*- 
#구글번역 

import time
import sys
import json
import io
import os
import requests
import googletrans
import traceback

#한글깨짐
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


MConfigData = sys.argv[1]
MConfig = json.loads(MConfigData)


NtosServer = MConfig['NtosServer']
CustId = MConfig['CustId']
it_id = MConfig['it_id']
TransStr = MConfig['TransStr']
OrgField = MConfig['OrgField']
TargetField = MConfig['TargetField']
g_dest = MConfig['g_dest']
g_src = MConfig['g_src']
ResultType = MConfig['ResultType']

try :
  translator = googletrans.Translator()
  ResultStr = translator.translate(TransStr, dest = str(g_dest), src = str(g_src))
  if ResultType == "View" :
    print(ResultStr)
  else :
    data = {'CustId':str(CustId), 'it_id':str(it_id), 'OrgField':str(OrgField), 'TargetField':str(TargetField), 'TransStr':str(TransStr), 'ResultStr':str(ResultStr.text) }
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    result = requests.post(NtosServer, data=json.dumps(data), headers=headers)
    print(result.text)
except :
  err = traceback.format_exc()
  print(str(err))
