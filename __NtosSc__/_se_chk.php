<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");
/*
셀레니움 실행 확인용
*/





exec("python3 /home/ntosmini/public_html/__NtosSc__/_se_chk.py", $ResultArr);
$PageHtml = implode("\n", $ResultArr);

echo $PageHtml;