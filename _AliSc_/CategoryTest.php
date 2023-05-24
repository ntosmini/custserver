<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");

$RunData = array();
$PATH = (empty($_GET['path']))?"":$_GET['path'];
$RunData['PathUsed'] = (empty($PATH))?"N":"Y";
$MConfigData = escapeshellarg(json_encode($RunData));
if(empty($PATH)){
  exec("python3 /home/ntosmini/public_html/_AliSc_/CategoryTest.v4.py {$MConfigData}", $ResultArr);
} else {
  echo $PATH;
  exec($PATH." python3 /home/ntosmini/public_html/_AliSc_/CategoryTest.v4.py {$MConfigData}", $ResultArr);
}

$PageHtml = implode("\n", $ResultArr);

echo $PageHtml;
