<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");
/*
상품 - 스트레이트
*/

$RunData = array();
$Ver = (empty($_POST['Ver']))?"v4":$_POST['Ver'];	//v3 or v4
$RunData['IslId_SiteUrl'] = (empty($_POST['IslId_SiteUrl']))?"":$_POST['IslId_SiteUrl'];
$RunData['CustId'] = (empty($_POST['CustId']))?"":$_POST['CustId'];

$RunData['FileSendSave'] = (empty($_POST['FileSendSave']))?"N":$_POST['FileSendSave'];	//파일 저장 전송 사용여부 Y/N
$RunData['NtosServer'] = (empty($_POST['NtosServer']))?"":$_POST['NtosServer'];	//받을 url
$RunData['UserAgent'] = (empty($_POST['UserAgent']))?"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36":$_POST['UserAgent'];
$RunData['ChromeVer'] = (empty($_POST['ChromeVer']))?"":$_POST['ChromeVer'];	//Chrome version

if(empty($Ver) || ($Ver != 'v3' && $Ver != 'v4') ){
	echo 'not Ver';
	exit;
}	//end if(empty($Ver))

if(empty($RunData['IslId_SiteUrl'])){
	echo 'not IslId_SiteUrl';
	exit;
}
$RunData['IslId_SiteUrl'] = explode("|^|", $RunData['IslId_SiteUrl']);

if(empty($RunData['CustId'])){
	echo 'not CustId';
	exit;
}

$MConfigData = escapeshellarg(json_encode($RunData));


exec("PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin python3 /home/ntosmini/public_html/_AliSc_/Item.{$Ver}.py {$MConfigData}");
