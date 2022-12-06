<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");
/*
카테고리 - 스트레이트
*/
$RunData = array();
$Ver = (empty($_POST['Ver']))?"v4":$_POST['Ver'];	//v3 or v4
$RunData['CslId_SiteUrl'] = (empty($_POST['CslId_SiteUrl']))?"":$_POST['CslId_SiteUrl'];
$RunData['CustId'] = (empty($_POST['CustId']))?"":$_POST['CustId'];
$RunData['Scroll'] = (empty($_POST['Scroll']))?"N":$_POST['Scroll'];	//스크롤
$RunData['ScrapServerId'] = (empty($_POST['ScrapServerId']))?"":$_POST['ScrapServerId'];	//server id


if(empty($Ver) || ($Ver != 'v3' && $Ver != 'v4') ){
	echo 'not Ver';
	exit;
}	//end if(empty($Ver))

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


exec("python3 /home/ntosmini/public_html/_AliSc_/Category.{$Ver}.py {$MConfigData}", $ResultArr);

$PageHtml = implode("\n", $ResultArr);

echo $PageHtml;
