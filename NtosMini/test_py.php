<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");

$url = (empty($_GET['url']))?"http://ntos.co.kr":$_GET['url'];

$url = base64_encode($url);

ob_start();
passthru("python3 /home/ntosmini/public_html/NtosMini/test_py.py $url");
$PageHtml = ob_get_clean(); 



echo $PageHtml;
