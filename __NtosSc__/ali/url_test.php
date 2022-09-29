<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");
/*
알리 카테고리 - 멀티
*/

$RunData = array();
$RunData['SiteUrl'] = (empty($_POST['SiteUrl']))?"":$_POST['SiteUrl'];



if( empty($RunData['SiteUrl']) ){
	echo 'error';
	exit;
}	//end if



$MConfigData = escapeshellarg(json_encode($RunData));




exec("python3 /home/ntosmini/public_html/__NtosSc__/ali/ali_cate_test.py {$MConfigData}", $ResultArr);
$PageHtml = implode("\n", $ResultArr);

echo $PageHtml;