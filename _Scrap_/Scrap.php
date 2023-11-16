<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");

$RunData = array();
$RunData['SiteUrl'] = (empty($_POST['SiteUrl']))?"":$_POST['SiteUrl'];
$RunData['SetAgent'] = (empty($_POST['SetAgent']))?"":$_POST['SetAgent'];

if(empty($RunData['SiteUrl'])){
	echo 'not SiteUrl';
	exit;
}

$MConfigData = escapeshellarg(json_encode($RunData));

exec("PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin python3 /home/ntosmini/public_html/_Scrap_/Scrap.py {$MConfigData}", $ResultArr);

$PageHtml = implode("\n", $ResultArr);
echo $PageHtml;
exit;