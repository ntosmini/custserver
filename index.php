<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");
/*
셀레니움 실행 확인용
*/
$Type = (empty($_GET['Type']))?"":$_GET['Type'];

if(empty($Type)){
	$PageHtml = "<div>ntoswebsuccess</div>";
	$PageHtml .= "<div>Type=(se or uc)</div>";
	$PageHtml .= "<div>SiteUrl=</div>";
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
	exec("PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin python3 /home/ntosmini/public_html/index.uc.py {$MConfigData}", $ResultArr);
	$PageHtml = implode("\n", $ResultArr);
} else {
	$PageHtml = "error : Type";
}
echo $PageHtml;
