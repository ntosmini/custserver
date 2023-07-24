<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");
/*
체크용 지우면 안됨
*/
$Type = (empty($_POST['Type']))?"":$_POST['Type']; //web, selenium
$CustId = (empty($_POST['CustId']))?"":$_POST['CustId']; //id
$SId = (empty($_POST['SId']))?"":$_POST['SId']; //server id
$NtosServer = (empty($_POST['NtosServer']))?"":$_POST['NtosServer']; //받을 url
$SiteUrl = (empty($_POST['SiteUrl']))?"":$_POST['SiteUrl'];
$ChromeVer = (empty($_POST['ChromeVer']))?"":$_POST['ChromeVer'];


if(empty($CustId)){
	echo 'not CustId';
	exit;
}

if(empty($NtosServer)){
	echo 'not NtosServer';
	exit;
}

if(empty($SiteUrl)){
	echo 'not SiteUrl';
	exit;
}

if(empty($Type)){
	echo 'not Type';
	exit;
}

if(empty($SId)){
	echo 'not SId';
	exit;
}

if($Type == "web"){
	$MiniServerGet['Type'] = $Type;
	$MiniServerGet['CustId'] = $CustId;
	$MiniServerGet['SId'] = $SId;
	$MiniServerGet['PageHtml'] = "ntoswebsuccess";

	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, $NtosServer );
	curl_setopt($ch, CURLOPT_HEADER, false);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
	curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
	curl_setopt($ch, CURLOPT_AUTOREFERER, true);
	curl_setopt($ch, CURLOPT_POST, true);
	curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($MiniServerGet));
	curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 300); //
	curl_setopt($ch, CURLOPT_TIMEOUT, 300); //
	$PageHtml=curl_exec($ch);
	$http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
	curl_close($ch);
	echo $PageHtml;
	exit;

} else if($Type == "selenium"){
	$RunData['Type'] = $Type;
	$RunData['SiteUrl'] = $SiteUrl;
	$RunData['CustId'] = $CustId;
	$RunData['SId'] = $SId;
	$RunData['NtosServer'] = $NtosServer;
	$RunData['SiteUrl'] = $SiteUrl;
	$RunData['ChromeVer'] = $ChromeVer;

	$MConfigData = escapeshellarg(json_encode($RunData));
	exec("PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin python3 /home/ntosmini/public_html/_NtosSc_/ServerChk.py {$MConfigData}", $ResultArr);
	$PageHtml = implode("\n", $ResultArr);
	echo $PageHtml;
	exit;
} else {
	$PageHtml = 'not Type';
}
echo $PageHtml;
