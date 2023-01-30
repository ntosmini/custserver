<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");
/*
Scrap
*/

$RunData = array();
$Ver = (empty($_POST['Ver']))?"v4":$_POST['Ver'];	//v3 or v4
$RunData['RunId_SiteUrl'] = (empty($_POST['RunId_SiteUrl']))?"":$_POST['RunId_SiteUrl'];
$RunData['CustId'] = (empty($_POST['CustId']))?"":$_POST['CustId'];
$RunData['ScrapType'] = (empty($_POST['ScrapType']))?"":$_POST['ScrapType'];  //prod or cate

$RunData['FileSaveDir'] = (empty($_POST['FileSaveDir']))?"N":$_POST['FileSaveDir']; //파일저장 폴더
$RunData['FileSave'] = (empty($_POST['FileSave']))?"N":$_POST['FileSave'];	//파일 저장 사용여부 Y/N
$RunData['NtosServer'] = (empty($_POST['NtosServer']))?"":$_POST['NtosServer'];	//파일 저장 후 전송시 받을 url


if(empty($Ver) || ($Ver != 'v3' && $Ver != 'v4') ){
	echo 'not Ver';
	exit;
}	//end if(empty($Ver))

if(empty($RunData['RunId_SiteUrl'])){
	echo 'not RunId_SiteUrl';
	exit;
}
$RunData['RunId_SiteUrl'] = explode("|^|", $RunData['RunId_SiteUrl']);

if(empty($RunData['CustId'])){
	echo 'not CustId';
	exit;
}

if(empty($RunData['ScrapType'])){
	echo 'not ScrapType';
	exit;
}

$MConfigData = escapeshellarg(json_encode($RunData));


exec("python3 /home/ntosmini/public_html/_NtosSc_/Scrap.{$Ver}.py {$MConfigData}", $ResultArr);

$PageHtml = implode("\n", $ResultArr);

echo $PageHtml;
