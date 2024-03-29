<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");
/*
상품 - 모바일
*/

$RunData = array();
$ScrapType =(empty($_POST['ScrapType']))?"":$_POST['ScrapType'];  // curl / selenium / uc
$RunData['CustId'] = (empty($_POST['CustId']))?"":$_POST['CustId'];
$RunData['SiteUrlList'] = (empty($_POST['SiteUrlList']))?"":$_POST['SiteUrlList'];
$RunData['FileSendSave'] = (empty($_POST['FileSendSave']))?"n":$_POST['FileSendSave'];	//파일 저장 전송 사용여부 y/n
$RunData['NtosServer'] = (empty($_POST['NtosServer']))?"":$_POST['NtosServer'];	//받을 url
$RunData['FileDir']  =(empty($_POST['FileDir']))?"":$_POST['FileDir'];  //저장폴더
$RunData['CookiesLang']  =(empty($_POST['CookiesLang']))?"":$_POST['CookiesLang'];  //언어 및 통화 (ko | en)

//셀레니움
$RunData['Scroll']  =(empty($_POST['Scroll']))?"n":$_POST['Scroll'];  //스크롤
$RunData['StartUrl']  =(empty($_POST['StartUrl']))?"":$_POST['StartUrl'];  //시작URL
$RunData['ChromeVer']  =(empty($_POST['ChromeVer']))?"":$_POST['ChromeVer'];  //크롬버전
$RunData['LockSlider']  =(empty($_POST['LockSlider']))?"n":$_POST['LockSlider'];  //LockSlider 사용여부(y/n)



if(empty($RunData['SiteUrlList'])){
	echo 'not SiteUrlList';
	exit;
}
$RunData['SiteUrlList'] = explode("|^|", $RunData['SiteUrlList']);

if(empty($RunData['CustId'])){
	echo 'not CustId';
	exit;
}
if(empty($RunData['FileDir'])){
	echo 'not FileDir';
	exit;
}
$MConfigData = escapeshellarg(json_encode($RunData));

switch($ScrapType){
	case 'curl' :
		exec("python3 /home/ntosmini/public_html/_AliScM_/Item.curl.py {$MConfigData}", $ResultArr);
	break;
	case 'uc' :
		exec("PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin python3 /home/ntosmini/public_html/_AliScM_/Item.uc.py {$MConfigData}", $ResultArr);
	break;
	default :
		exec("python3 /home/ntosmini/public_html/_AliScM_/Item.selenium.py {$MConfigData}", $ResultArr);
	break;
}
if(isset($ResultArr) && count($ResultArr) > 0){
	$PageHtml = implode("\n", $ResultArr);
	echo $PageHtml;
}
