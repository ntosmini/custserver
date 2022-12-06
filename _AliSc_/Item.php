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
$RunData['ScrapServerId'] = (empty($_POST['ScrapServerId']))?"":$_POST['ScrapServerId'];	//server id


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


exec("python3 /home/ntosmini/public_html/_AliSc_/Item.{$Ver}.py {$MConfigData}", $ResultArr);

$PageHtml = implode("\n", $ResultArr);

echo $PageHtml;
