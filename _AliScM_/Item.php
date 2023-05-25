<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");
/*
상품 - 모바일
*/

$RunData = array();
$ScrapType =(empty($_POST['ScrapType']))?"":$_POST['ScrapType'];  // curl / selenium / uc
$RunData['CustId'] = (empty($_POST['CustId']))?"":$_POST['CustId'];
$RunData['IslId_SiteUrl'] = (empty($_POST['IslId_SiteUrl']))?"":$_POST['IslId_SiteUrl'];
$RunData['FileSendSave'] = (empty($_POST['FileSendSave']))?"N":$_POST['FileSendSave'];	//파일 저장 전송 사용여부 Y/N
$RunData['NtosServer'] = (empty($_POST['NtosServer']))?"":$_POST['NtosServer'];	//받을 url
$RunData['FileDir']  =(empty($_POST['FileDir ']))?"":$_POST['FileDir '];  //저장폴더
$RunData['UserAgent'] = (empty($_POST['UserAgent']))?"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36":$_POST['UserAgent'];




if(empty($RunData['IslId_SiteUrl'])){
	echo 'not IslId_SiteUrl';
	exit;
}
$RunData['IslId_SiteUrl'] = explode("|^|", $RunData['IslId_SiteUrl']);

if(empty($RunData['CustId'])){
	echo 'not CustId';
	exit;
}
if(empty($RunData['FileDir'])){
	echo 'not FileDir';
	exit;
}
$MConfigData = escapeshellarg(json_encode($RunData));


