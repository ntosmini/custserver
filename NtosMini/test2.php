<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");

#$command = escapeshellcmd('python3 /home/ntosmini/public_html/NtosMini_U/test.py');
#$output = shell_exec($command);
#echo $output;
#exit;

$SiteUrl = (empty($_GET['SiteUrl']))?"not":$_GET['SiteUrl'];
$SiteUrl = base64_encode($SiteUrl);

	ob_start();
	passthru("python3 /home/ntosmini/public_html/NtosMini/test2.py $SiteUrl");
	//exec("python3 /home/ntosmini/public_html/NtosMini/test.py")
	$PageHtml = ob_get_clean(); 


echo $PageHtml;
