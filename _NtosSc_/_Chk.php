<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");
/*
체크용 지우면 안됨
*/
exec("PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin python3 /home/ntosmini/public_html/_NtosSc_/_Chk.py", $ResultArr);
$PageHtml = implode("\n", $ResultArr);

echo $PageHtml;
