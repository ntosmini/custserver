<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");
/*
서버체크
*/
$RunData = array();
$Ver = (empty($_POST['Ver']))?"v4":$_POST['Ver'];	//v3 or v4
$RunData['CustId'] = (empty($_POST['CustId']))?"":$_POST['CustId'];
$RunData['SiteUrl'] = (empty($_POST['SiteUrl']))?"http://product.ntos.co.kr/_SeleniumChk.php":$_POST['SiteUrl'];
$RunData['NtosServer'] = (empty($_POST['NtosServer']))?"":$_POST['NtosServer'];	//받을 url


if(empty($Ver) || ($Ver != 'v3' && $Ver != 'v4') ){
	echo 'not Ver';
	exit;
}	//end if(empty($Ver))

if(empty($RunData['SiteUrl'])){
	echo 'not SiteUrl';
	exit;
}

if(empty($RunData['NtosServer'])){
	echo 'not NtosServer';
	exit;
}

if(empty($RunData['CustId'])){
	echo 'not CustId';
	exit;
}

$MConfigData = escapeshellarg(json_encode($RunData));


exec("python3 /home/ntosmini/public_html/_AliSc_/_ServerChk.{$Ver}.py {$MConfigData}", $ResultArr);