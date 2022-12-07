<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");
/*
셀레니움 실행 확인용
*/
$Type = (empty($_GET['Type']))?"":$_GET['Type'];
$Ver = (empty($_GET['Ver']))?"":$_GET['Ver'];	//v3 or v4


if(empty($Type)){
	$PageHtml = "ntoswebsuccess";
} else if($Type == "py"){
	if($Ver == "v4" || $Ver == "v3"){
		$RunData = array();
		$RunData['SiteUrl'] = (empty($_GET['SiteUrl']))?"http://product.ntos.co.kr/_SeleniumChk.php":$_GET['SiteUrl'];
		$RunData['log'] = (empty($_GET['log']))?"n":"y";
		$RunData['refresh'] = (empty($_GET['refresh']))?"n":"y";
		$MConfigData = escapeshellarg(json_encode($RunData));
		exec("python3 /home/ntosmini/public_html/index.{$Ver}.py {$MConfigData}", $ResultArr);
		$PageHtml = implode("\n", $ResultArr);
	} else {
		$PageHtml = "error : Not Ver";
	}
} else {
	$PageHtml = "error : Type";
}
echo $PageHtml;
