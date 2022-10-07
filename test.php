<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");
/*
알리 카테고리 - 멀티
*/



exec("python3 /home/ntosmini/public_html/test.php", $ResultArr);
$PageHtml = implode("\n", $ResultArr);

echo $PageHtml;
