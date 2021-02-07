<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");

	ob_start();
	passthru("python3 /home/ntos/public_html/_Selenium/keepa.py");
	$PageHtml = ob_get_clean(); 


echo $PageHtml;
