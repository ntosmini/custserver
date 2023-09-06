<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");

$Type = (empty($_POST['Type']))?"server":$_POST['Type'];
$Search = (empty($_POST['Search']))?"n":$_POST['Search'];
$SearchChk = (empty($_POST['SearchChk']))?"n":$_POST['SearchChk'];

exec("PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin python3 /home/ntosmini/public_html/_Scrap_/mitem.py {$Type} {$Search} {$SearchChk}", $ResultArr);
$PageHtml = implode("\n", $ResultArr);
$PageHtml = strip_tags($PageHtml);
echo $PageHtml;
