<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");
/*
알리 카테고리 - 멀티
*/

$RunData = array();
$RunData['SiteUrl'] = (empty($_POST['SiteUrl']))?"":$_POST['SiteUrl'];
$RunData['WebType'] = (empty($_POST['WebType']))?"":$_POST['WebType'];



if( empty($RunData['SiteUrl']) ){
	echo 'error';
	exit;
}	//end if

if($RunData['WebType'] == "phpcurl"){
	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, $SiteUrl );
	curl_setopt($ch, CURLOPT_HEADER, false);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
	curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
	curl_setopt($ch, CURLOPT_AUTOREFERER, true);
	
	$Agent = ($Agent == "not")?"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36":$Agent;
	curl_setopt($ch, CURLOPT_USERAGENT, $Agent);

	curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 120); //
	curl_setopt($ch, CURLOPT_TIMEOUT, 300); //
	$PageHtml=curl_exec($ch);
	curl_close($ch);
} else {

	$MConfigData = escapeshellarg(json_encode($RunData));




	exec("python3 /home/ntosmini/public_html/__NtosSc__/ali/url_test.py {$MConfigData}", $ResultArr);
	$PageHtml = implode("\n", $ResultArr);
}

echo $PageHtml;
