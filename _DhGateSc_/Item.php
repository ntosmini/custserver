<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");
/*
상품 - 스트레이트
*/

$RunData = array();
$RunData['UserAgent'] = (empty($_POST['UserAgent']))?"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36":$_POST['UserAgent'];

$RunData['CustId'] = (empty($_POST['CustId']))?"":$_POST['CustId'];
if(empty($RunData['CustId'])){
	echo 'not CustId';
	exit;
}

$RunData['StartSiteUrl'] = (empty($_POST['StartSiteUrl']))?"":$_POST['StartSiteUrl'];	//시작 url
$RunData['SiteUrlOne'] = (empty($_POST['SiteUrlOne']))?"N":$_POST['SiteUrlOne'];
$RunData['SiteUrl_SaveFileName'] = (empty($_POST['SiteUrl_SaveFileName']))?"":$_POST['SiteUrl_SaveFileName'];	//수집url|@|저장파일명 or N -- 
$RunData['Refresh'] = ($_POST['Refresh'] == "Y")?$_POST['Refresh']:"N";;	//새로고침 - Y or N
$RunData['Scroll'] = ($_POST['Scroll'] == "Y")?$_POST['Scroll']:"N";	//스크롤 내리기 - Y or N
$RunData['ScrapResultType'] = (empty($_POST['ScrapResultType']))?"view":$_POST['ScrapResultType'];	//수집파일 방식 - save or send or view
$RunData['ChromeVer'] = (empty($_POST['ChromeVer']))?"":$_POST['ChromeVer'];	//Chrome version

if($RunData['SiteUrlOne'] == "N" && $RunData['ScrapResultType'] == "view"){
	echo "not SiteUrlOne : ".$RunData['SiteUrlOne'].", ScrapResultType : ".$RunData['ScrapResultType'];
	exit;
}

$RunData['FileSaveDir'] = (($RunData['ScrapResultType'] == "save" || $RunData['ScrapResultType'] == "send") && $_POST['FileSaveDir'])?$_POST['FileSaveDir']:"";
if(empty($RunData['FileSaveDir']) && ($RunData['ScrapResultType'] == "save" || $RunData['ScrapResultType'] == "send")){
	echo "not FileSaveDir (".$RunData['ScrapResultType'].")";
	exit;
}

$RunData['NtosSendServer'] = ($RunData['ScrapResultType'] == "send" && $_POST['NtosSendServer'])?$_POST['NtosSendServer']:"";	//전송서버 폴더까지
if(empty($RunData['NtosSendServer']) && $RunData['ScrapResultType'] == "send"){
	echo "not NtosSendServer (".$RunData['ScrapResultType'].")";
	exit;
}

$RunData['SiteUrl_SaveFileName'] = explode("|^|", $RunData['SiteUrl_SaveFileName']);
$MConfigData = escapeshellarg(json_encode($RunData));

exec("PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin python3 /home/ntosmini/public_html/_DhGateSc_/Item.py {$MConfigData}");
