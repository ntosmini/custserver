<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");
$ChromeVer = (empty($_GET['ChromeVer']))?"":$_GET['ChromeVer'];

if(empty($ChromeVer)){
  exec("PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin python3 /home/ntosmini/public_html/test.py", $ResultArr);
} else {
  $RunData['ChromeVer'] = $ChromeVer;
  $MConfigData = escapeshellarg(json_encode($RunData));
  exec("PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin python3 /home/ntosmini/public_html/testver.py {$MConfigData}", $ResultArr);
}
$PageHtml = implode("\n", $ResultArr);
echo $PageHtml;
