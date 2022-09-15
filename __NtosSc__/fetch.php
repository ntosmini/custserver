<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");
/*
전체 패치
*/





exec("python3 /home/ntosmini/public_html/__NtosSc__/fetch.py", $ResultArr);
$PageHtml = implode("\n", $ResultArr);

echo $PageHtml;
