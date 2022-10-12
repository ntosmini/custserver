<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");
/*
Scrap 폴더
*/
$Ver = (empty($_POST['Ver']))?"":$_POST['Ver'];	//v3 or v4
$SiteUrl = $_POST['SiteUrl'];

if(empty($SiteUrl)){
  $PageHtml = "not SiteUrl"; 
} else {
  exec("python3 /home/ntosmini/public_html/Scrap.{$Ver}.py {$SiteUrl}", $ResultArr);
  $PageHtml = implode("\n", $ResultArr);
}
