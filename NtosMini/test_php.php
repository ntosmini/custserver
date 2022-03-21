<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");

$url = (empty($_GET['url']))?"http://ntos.co.kr":$_GET['url'];

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url );
curl_setopt($ch, CURLOPT_HEADER, false);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_AUTOREFERER, true);
curl_setopt($ch, CURLOPT_USERAGENT, "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36");
curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 120); //
curl_setopt($ch, CURLOPT_TIMEOUT, 300); //
$PageHtml=curl_exec($ch);
curl_close($ch);

echo $PageHtml;
