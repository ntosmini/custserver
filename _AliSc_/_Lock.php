<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");

$RunData = array();

$RunData['UserAgent'] = (empty($_POST['UserAgent']))?"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36":$_POST['UserAgent'];
$RunData['SiteUrl'] = (empty($_POST['SiteUrl']))?"":$_POST['SiteUrl'];	//사이트 url

$RunData['LockChkUsed'] = (empty($_POST['LockChkUsed']))?"N":"Y";	//lock chk
$ChromeType = (empty($_POST['ChromeType']))?"":$_POST['ChromeType'];
if(empty($RunData['SiteUrl'])){
	echo 'not SiteUrl';
	exit;
}

$MConfigData = escapeshellarg(json_encode($RunData));

if($ChromeType == "uc"){
	exec("PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin python3 /home/ntosmini/public_html/_Scrap_/_Lock.uc.py {$MConfigData}", $ResultArr);		
	$PageHtml = implode("\n", $ResultArr);
} else if($ChromeType == "curl"){
	
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $RunData['SiteUrl'] );
curl_setopt($ch, CURLOPT_HEADER, false);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_AUTOREFERER, true);

curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 300); //
curl_setopt($ch, CURLOPT_TIMEOUT, 300); //
$PageHtml=curl_exec($ch);
$http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);
	
} else {
	exec("python3 /home/ntosmini/public_html/_Scrap_/Scrap.py {$MConfigData}", $ResultArr);
	$PageHtml = implode("\n", $ResultArr);
}


echo $PageHtml;
