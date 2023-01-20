<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");
/*
Scrap 폴더
*/
$Ver = (empty($_POST['Ver']))?"":$_POST['Ver'];	//v3 or v4
$RunData['CustId'] = (empty($_POST['CustId']))?"":$_POST['CustId'];
$RunData['DataId'] = (empty($_POST['DataId']))?"":$_POST['DataId'];
$RunData['SiteUrl'] = (empty($_POST['SiteUrl']))?"":$_POST['SiteUrl'];
$RunData['Scroll'] = (empty($_POST['Scroll']))?"N":$_POST['Scroll']; //Y,N

$RunData['Refresh'] = (empty($_POST['Refresh']))?"N":$_POST['Refresh']; //Y,N

$RunData['FileSaveSendUrl'] = (empty($_POST['FileSaveSendUrl']))?"N":$_POST['FileSaveSendUrl']; //N, URL

if(empty($RunData['SiteUrl'])){
  $PageHtml = "not SiteUrl"; 
} else {
  $MConfigData = escapeshellarg(json_encode($RunData));
  exec("python3 /home/ntosmini/public_html/_NtosSc_/Scrap.{$Ver}.py {$MConfigData}", $ResultArr);
  $PageHtml = implode("\n", $ResultArr);
}
echo $PageHtml;
