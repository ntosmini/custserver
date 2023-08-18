<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");

exec("PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin python3 /home/ntosmini/public_html/Test/alilogin.py", $ResultArr);

if(isset($ResultArr) && count($ResultArr) > 0){
	$PageHtml = implode("\n", $ResultArr);
	echo $PageHtml;
}
