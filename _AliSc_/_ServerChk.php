<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");
/*
서버체크
*/
$RunData = array();
$Type = (empty($_POST['Type']))?"":$_POST['Type'];
$Ver = (empty($_POST['Ver']))?"v4":$_POST['Ver'];	//v3 or v4
$RunData['CustId'] = (empty($_POST['CustId']))?"":$_POST['CustId'];
$RunData['SiteUrl'] = (empty($_POST['SiteUrl']))?"http://product.ntos.co.kr/_SeleniumChk.php":$_POST['SiteUrl'];
$RunData['Server'] = (empty($_POST['Server']))?"":$_POST['Server'];	//통신 서버
$RunData['ReturnUrl'] = (empty($_POST['ReturnUrl']))?"":$_POST['ReturnUrl'];	//받을 url
$RunData['Sid'] = (empty($_POST['Sid']))?"":$_POST['Sid'];	//서버 ID


if(empty($Type)){
	echo 'not Type';
	exit;
}

if($Type == "web"){
	echo "ntoswebsuccess";
	exit;
}


if(empty($Ver) || ($Ver != 'v3' && $Ver != 'v4') ){
	echo 'not Ver';
	exit;
}	//end if(empty($Ver))

if(empty($RunData['CustId'])){
	echo 'not CustId';
	exit;
}

if(empty($RunData['SiteUrl'])){
	echo 'not SiteUrl';
	exit;
}

if(empty($RunData['Server'])){
	echo 'not Server';
	exit;
}

if(empty($RunData['ReturnUrl'])){
	echo 'not ReturnUrl';
	exit;
}

if(empty($RunData['Sid'])){
	echo 'not Sid';
	exit;
}



$MConfigData = escapeshellarg(json_encode($RunData));


exec("python3 /home/ntosmini/public_html/_AliSc_/_ServerChk.{$Ver}.py {$MConfigData}", $ResultArr);
