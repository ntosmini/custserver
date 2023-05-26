<?php

set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");

$file_name = "mecotine_click.py";

if(isset($_GET["M"]))
    $file_name = "mecotine_m_click.py";

exec("PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin python3 /home/ntosmini/public_html/_Mecotine_/{$file_name}", $ResultArr);

echo implode("\n",$ResultArr);