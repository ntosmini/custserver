<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");

$Type = (empty($_GET['Type']))?"web":$_GET['Type']; //web, selenium
$Ver = (empty($_GET['Ver']))?"":$_GET['Ver'];	//v3 or v4
$SiteUrl = urldecode($_GET['SiteUrl']);

$PageHtml = '';
if(empty($SiteUrl)){
   $PageHtml = 'not SiteUrl';
} else {
  if($Type == "web"){
    $PageHtml = 'ntoswebsuccess';
  } else if($Type == "selenium"){
    $RunData['SiteUrl'] = $SiteUrl;
		$MConfigData = escapeshellarg(json_encode($RunData));
		exec("python3 /home/ntosmini/public_html/_NtosSc_/ServerChk.{$Ver}.py {$MConfigData}", $ResultArr);
		$PageHtml = implode("\n", $ResultArr);
  } else {
    $PageHtml = 'not Type';
  }
}
echo $PageHtml;
