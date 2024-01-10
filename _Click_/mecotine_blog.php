<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");

$RunData = array();
$RunData['Type'] = (empty($_POST['Type']))?"server":$_POST['Type'];
$RunData['SiteUrl'] = (empty($_POST['SiteUrl']))?"":$_POST['SiteUrl'];
$RunData['Search'] = (empty($_POST['Search1']))?"":$_POST['Search1'];
$RunData['SearchChk'] = (empty($_POST['SearchChk']))?"":$_POST['SearchChk'];


if(empty($RunData['SiteUrl'])){
	echo 'not SiteUrl';
	exit;
}


if(empty($RunData['SearchChk'])){
	echo 'not SearchChk';
	exit;
}

$MConfigData = escapeshellarg(json_encode($RunData));

exec("PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin python3 /home/ntosmini/public_html/_Click_/mecotine_blog.py {$MConfigData}", $ResultArr);

$PageHtml = implode("\n", $ResultArr);
echo $PageHtml;
exit;