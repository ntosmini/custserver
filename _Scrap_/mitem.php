<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");

$RunData = array();
$RunData['Type'] = (empty($_POST['Type']))?"server":$_POST['Type'];
$RunData['SelectHref'] = (empty($_POST['SelectHref']))?"n":$_POST['SelectHref'];
$RunData['Search1'] = (empty($_POST['Search1']))?"n":$_POST['Search1'];
$RunData['Search2'] = (empty($_POST['Search2']))?"n":$_POST['Search2'];
$RunData['Search3'] = (empty($_POST['Search3']))?"n":$_POST['Search3'];

$MConfigData = escapeshellarg(json_encode($RunData));

exec("PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin python3 /home/ntosmini/public_html/_Scrap_/mitem.py {$MConfigData}", $ResultArr);
$PageHtml = implode("\n", $ResultArr);
$PageHtml = strip_tags($PageHtml);
echo $PageHtml;
