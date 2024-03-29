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
$RunData['FileDir']  =(empty($_POST['FileDir']))?"":$_POST['FileDir'];  //저장폴더
$RunData['UserAgent'] = (empty($_GET['UserAgent']))?"Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36":$_GET['UserAgent'];
$RunData['LangType']  =(empty($_POST['LangType']))?"":$_POST['LangType'];  //언어 및 통화 (ko | en)
$RunData['ChromeVer'] = (empty($_POST['ChromeVer']))?"":$_POST['ChromeVer'];	//Chrome version



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

switch($ScrapType){
	case 'curl' :
		exec("python3 /home/ntosmini/public_html/_AliScM_/ItemM.curl.py {$MConfigData}", $ResultArr);
	break;
	case 'uc' :
		exec("PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin python3 /home/ntosmini/public_html/_AliScM_/ItemM.uc.py {$MConfigData}", $ResultArr);
	break;
	default :
		exec("python3 /home/ntosmini/public_html/_AliScM_/ItemM.selenium.py {$MConfigData}", $ResultArr);
	break;
}
if(isset($ResultArr) && count($ResultArr) > 0){
	$PageHtml = implode("\n", $ResultArr);
	echo $PageHtml;
}
