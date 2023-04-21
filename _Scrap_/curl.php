<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");

$SiteUrl = empty($_GET['SiteUrl']))?"":$_GET['SiteUrl'];
$Agent = empty($_GET['Agent']))?"":$_GET['Agent'];

if(empty($SiteUrl)){
  echo 'not SiteUrl'; 
  exit;
}

$SiteUrl = base64_encode($SiteUrl);
$Agent = base64_encode($Agent);

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $SiteUrl );
curl_setopt($ch, CURLOPT_HEADER, false);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
if($Agent){
  curl_setopt($ch, CURLOPT_USERAGENT, $Agent);
} else {
  curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36');
}
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_AUTOREFERER, true);
curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 300); //
curl_setopt($ch, CURLOPT_TIMEOUT, 300); //
$PageHtml=curl_exec($ch);
$http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

echo $PageHtml;
