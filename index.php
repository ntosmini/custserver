<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");
/*
셀레니움 실행 확인용
*/
$Type = (empty($_GET['Type']))?"":$_GET['Type'];
$Ver = (empty($_GET['Ver']))?"":$_GET['Ver'];	//v3 or v4


if(empty($Type)){
	$PageHtml = "success";
} else if($Type == "py"){
	if($Ver == "v4" || $Ver == "v3"){
		$RunData = array();
		$RunData['SiteUrl'] = (empty($_GET['SiteUrl']))?"http://mini.ntos.co.kr/_se_chk.html":$_GET['SiteUrl'];
		$MConfigData = escapeshellarg(json_encode($RunData));
		exec("python3 /home/ntosmini/public_html/_test.{$Ver}.py {$MConfigData}", $ResultArr);
		$PageHtml = implode("\n", $ResultArr);
	} else {
		$PageHtml = "error : Not Ver";
	}
} else {
	$PageHtml = "error : Type";
}
echo $PageHtml;
