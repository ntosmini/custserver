<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");
/*
체크용 지우면 안됨
*/
$Type = (empty($_GET['Type']))?"web":$_GET['Type']; //web, selenium
$Ver = (empty($_GET['Ver']))?"":$_GET['Ver'];	//v3 or v4
$SiteUrl = (empty($_GET['SiteUrl']))?"":urldecode($_GET['SiteUrl']);

$PageHtml = '';
if($Type == "web"){
	$PageHtml = 'ntoswebsuccess';
} else if($Type == "selenium"){
	$RunData['SiteUrl'] = $SiteUrl;
	$MConfigData = escapeshellarg(json_encode($RunData));
	exec("PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin python3 /home/ntosmini/public_html/_NtosSc_/ServerChk.py {$MConfigData}", $ResultArr);
	$PageHtml = implode("\n", $ResultArr);
} else {
	$PageHtml = 'not Type';
}
echo $PageHtml;
