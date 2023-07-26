<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");
/*
알리 카테고리 - 모바일
*/

$RunData = array();
$ScrapType =(empty($_POST['ScrapType']))?"":$_POST['ScrapType'];  // curl / selenium / uc
$RunData['CustId'] = (empty($_POST['CustId']))?"":$_POST['CustId'];
$RunData['SiteUrlList'] = (empty($_POST['SiteUrlList']))?"":$_POST['SiteUrlList'];
$RunData['FileSendSave'] = (empty($_POST['FileSendSave']))?"N":$_POST['FileSendSave'];	//파일 저장 전송 사용여부 Y/N
$RunData['NtosServer'] = (empty($_POST['NtosServer']))?"":$_POST['NtosServer'];	//받을 url
$RunData['FileDir']  =(empty($_POST['FileDir']))?"":$_POST['FileDir'];  //저장폴더
$RunData['LangType']  =(empty($_POST['LangType']))?"":$_POST['LangType'];  //언어 및 통화 (ko | en)

//셀레니움
$RunData['Scroll']  =(empty($_POST['Scroll']))?"N":$_POST['Scroll'];  //스크롤
$RunData['StartUrl']  =(empty($_POST['StartUrl']))?"":$_POST['StartUrl'];  //시작URL
$RunData['ChromeVer']  =(empty($_POST['ChromeVer']))?"":$_POST['ChromeVer'];  //크롬버전



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
		echo "1";
		exec("python3 /home/ntosmini/public_html/_AliScM_/Category.curl.py {$MConfigData}", $ResultArr);
	break;
	case 'uc' :
		echo "2";
		exec("PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin python3 /home/ntosmini/public_html/_AliScM_/Category.uc.py {$MConfigData}", $ResultArr);
	break;
	default :
		echo "3";
		exec("python3 /home/ntosmini/public_html/_AliScM_/Category.selenium.py {$MConfigData}", $ResultArr);
	break;
}
if(isset($ResultArr) && count($ResultArr) > 0){
	$PageHtml = implode("\n", $ResultArr);
	echo $PageHtml;
}
