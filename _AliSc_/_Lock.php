<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");

$RunData = array();

$RunData['UserAgent'] = (empty($_POST['UserAgent']))?"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36":$_POST['UserAgent'];
$RunData['SiteUrl'] = (empty($_POST['SiteUrl']))?"":$_POST['SiteUrl'];	//사이트 url

$RunData['LockChk'] = (empty($_POST['LockChk']))?"N":"Y";	//lock chk

if(empty($RunData['SiteUrl'])){
	echo 'not SiteUrl';
	exit;
}

$MConfigData = escapeshellarg(json_encode($RunData));

exec("python3 /home/ntosmini/public_html/_AliSc_/_Lock.py {$MConfigData}", $ResultArr);

$PageHtml = implode("\n", $ResultArr);

echo $PageHtml;