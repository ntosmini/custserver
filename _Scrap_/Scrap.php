<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");

$RunData = array();
$ScrapType = (empty($_POST['ScrapType']))?"uc":$_POST['ScrapType'];	//수집방식 - curl or self or selenium or pyget
$RunData['SiteUrl'] = (empty($_POST['SiteUrl']))?"":$_POST['SiteUrl'];


if(empty($RunData['SiteUrl'])){
	echo 'not SiteUrl';
	exit;
}

switch($ScrapType){
	case 'uc' :
		exec("PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin python3 /home/ntosmini/public_html/_Scrap_/Scrap.uc.py {$MConfigData}", $ResultArr);
	break;

	default :
		echo "ntoswebsuccess";
		exit;
	break;
}
$PageHtml = implode("\n", $ResultArr);
echo $PageHtml;
exit;
