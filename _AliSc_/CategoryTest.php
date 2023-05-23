<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");
$PATH = (empty($_GET['path']))?"":$_GET['path'];
if(empty($PATH)){
  exec("python3 /home/ntosmini/public_html/_AliSc_/CategoryTest.v4.py", $ResultArr);
} else {
  exec($PATH." python3 /home/ntosmini/public_html/_AliSc_/CategoryTest.v4.py", $ResultArr);
}

$PageHtml = implode("\n", $ResultArr);

echo $PageHtml;
