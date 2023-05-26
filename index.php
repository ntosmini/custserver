<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");
/*
셀레니움 실행 확인용
*/
$Type = (empty($_GET['Type']))?"":$_GET['Type'];

if(empty($Type)){
	$PageHtml = "ntoswebsuccess";
} else if($Type == "se"){
	$RunData = array();
	$RunData['SiteUrl'] = (empty($_GET['SiteUrl']))?"http://product.ntos.co.kr/_SeleniumChk.php":urldecode($_GET['SiteUrl']);
	$MConfigData = escapeshellarg(json_encode($RunData));
	exec("python3 /home/ntosmini/public_html/index.se.py {$MConfigData}", $ResultArr);
	$PageHtml = implode("\n", $ResultArr);
} else if($Type == "uc"){
	$RunData = array();
	$RunData['SiteUrl'] = (empty($_GET['SiteUrl']))?"http://product.ntos.co.kr/_SeleniumChk.php":urldecode($_GET['SiteUrl']);
	$MConfigData = escapeshellarg(json_encode($RunData));
	exec("python3 /home/ntosmini/public_html/index.uc.py {$MConfigData}", $ResultArr);
	$PageHtml = implode("\n", $ResultArr);
} else {
	$PageHtml = "error : Type";
}
echo $PageHtml;
