<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");

$RunData = array();
$PATH = (empty($_GET['path']))?"":$_GET['path'];
$RunData['PathUsed'] = (empty($PATH))?"N":"Y";
$MConfigData = escapeshellarg(json_encode($RunData));
if(empty($PATH)){
  echo 'Selenium<br>';
  echo 'undetected_chromedriver 사용시 ?path=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin<br><br>';
  exec("python3 /home/ntosmini/public_html/_AliSc_/CategoryTest.v4.py {$MConfigData}", $ResultArr);
} else {
  echo 'undetected_chromedriver<br>';
  exec("PATH=".$PATH." python3 /home/ntosmini/public_html/_AliSc_/CategoryTest.v4.py {$MConfigData}", $ResultArr);
}

$PageHtml = implode("\n", $ResultArr);

echo $PageHtml;
