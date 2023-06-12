<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");
/*
카테고리 - 스트레이트
*/
$RunData = array();
$RunData['CslId_SiteUrl'] = (empty($_POST['CslId_SiteUrl']))?"":$_POST['CslId_SiteUrl'];
$RunData['CustId'] = (empty($_POST['CustId']))?"":$_POST['CustId'];
$RunData['Scroll'] = (empty($_POST['Scroll']))?"N":$_POST['Scroll'];	//스크롤

$RunData['FileSendSave'] = (empty($_POST['FileSendSave']))?"N":$_POST['FileSendSave'];	//파일 저장 전송 사용여부 Y/N
$RunData['NtosServer'] = (empty($_POST['NtosServer']))?"":$_POST['NtosServer'];	//받을 url
$RunData['UserAgent'] = (empty($_POST['UserAgent']))?"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36":$_POST['UserAgent'];
$RunData['FileSaveDir'] = (empty($_POST['FileSaveDir']))?"":$_POST['FileSaveDir'];	//xs 서버 저장 폴더

$RunData['CookiesLang'] = (empty($_POST['CookiesLang']))?"":$_POST['CookiesLang'];	//쿠키 언어
$RunData['ChromeVer'] = (empty($_POST['ChromeVer']))?"":$_POST['ChromeVer'];	//Chrome version


if(empty($RunData['CslId_SiteUrl'])){
	echo 'not CslId_SiteUrl';
	exit;
}
$RunData['CslId_SiteUrl'] = explode("|^|", $RunData['CslId_SiteUrl']);

if(empty($RunData['CustId'])){
	echo 'not CustId';
	exit;
}

$MConfigData = escapeshellarg(json_encode($RunData));

if(empty($RunData['CookiesLang'])){
	exec("PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin python3 /home/ntosmini/public_html/_AliSc_/Category.py {$MConfigData}");
} else {
	exec("PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin python3 /home/ntosmini/public_html/_AliSc_/Category.Cookies.py {$MConfigData}");
}
