<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");

$RunData = array();
$ScrapType = (empty($_POST['ScrapType']))?"uc":$_POST['ScrapType'];  //uc(selenium) / curl
$RunData['SiteUrlArr'] = (empty($_POST['SiteUrlArr']))?"":$_POST['SiteUrlArr'];
$RunData['CustId'] = (empty($_POST['CustId']))?"":$_POST['CustId'];
$RunData['FileSaveDir'] = (empty($_POST['FileSaveDir']))?"":$_POST['FileSaveDir'];	//xs 서버 저장 폴더

$RunData['FileSendSave'] = (empty($_POST['FileSendSave']))?"n":$_POST['FileSendSave'];	//파일 저장 전송 사용여부 y/n
$RunData['NtosServer'] = (empty($_POST['NtosServer']))?"":$_POST['NtosServer'];	//받을 url

$RunData['UserAgent'] = (empty($_POST['UserAgent']))?"":$_POST['UserAgent'];
$RunData['ChromeVer'] = (empty($_POST['ChromeVer']))?"":$_POST['ChromeVer'];	//Chrome version	2023-07-19 = 114

if(empty($RunData['SiteUrlArr'])){
	echo 'not SiteUrlArr';
	exit;
}

if(empty($RunData['CustId'])){
	echo 'not CustId';
	exit;
}

$RunData['SiteUrlArr'] = explode("|^|", $RunData['SiteUrlArr']);
$MConfigData = escapeshellarg(json_encode($RunData));

switch($ScrapType){
  case 'uc' :
    exec("PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin python3 /home/ntosmini/public_html/_NtosSc_/Scrap.uc.py {$MConfigData}");
  break;

  case 'curl' :
    exec("PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin python3 /home/ntosmini/public_html/_NtosSc_/Scrap.curl.py {$MConfigData}");
  break;

  default :
    exit;
  break;
}
