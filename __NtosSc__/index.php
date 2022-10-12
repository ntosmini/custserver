<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");
/*
Scrap 폴더
*/
$Ver = (empty($_POST['Ver']))?"":$_POST['Ver'];	//v3 or v4
$RunData['SiteUrl'] = (empty($_POST['SiteUrl']))?"":$_POST['SiteUrl'];

if(empty($RunData['SiteUrl'])){
  $PageHtml = "not SiteUrl"; 
} else {
  $MConfigData = escapeshellarg(json_encode($RunData));
  exec("python3 /home/ntosmini/public_html/__NtosSc__/Scrap.{$Ver}.py {$MConfigData}", $ResultArr);
  $PageHtml = implode("\n", $ResultArr);
}
echo $PageHtml;
