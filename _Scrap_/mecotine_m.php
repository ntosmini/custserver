<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");

$RunData = array();
$RunData['Type'] = (empty($_POST['Type']))?"server":$_POST['Type'];
$RunData['SiteUrl'] = (empty($_POST['SiteUrl']))?"":$_POST['SiteUrl'];
$RunData['Search1'] = (empty($_POST['Search1']))?"":$_POST['Search1'];
$RunData['Search2'] = (empty($_POST['Search2']))?"":$_POST['Search2'];
$RunData['SearchChk1'] = (empty($_POST['SearchChk1']))?"":$_POST['SearchChk1'];
$RunData['SearchChk2'] = (empty($_POST['SearchChk2']))?"":$_POST['SearchChk2'];


if(empty($RunData['SiteUrl'])){
	echo 'not SiteUrl';
	exit;
}

if(empty($RunData['Search2'])){
	echo 'not Search2';
	exit;
}

$MConfigData = escapeshellarg(json_encode($RunData));

exec("PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin python3 /home/ntosmini/public_html/_Scrap_/mecotine_m.py {$MConfigData}", $ResultArr);

$PageHtml = implode("\n", $ResultArr);
echo $PageHtml;
exit;
