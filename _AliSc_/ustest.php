<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");

exec("python3 /home/ntosmini/public_html/_AliSc_/ustest.py", $ResultArr);

$PageHtml = implode("\n", $ResultArr);

echo $PageHtml;
