<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");
/*
2022-09-01
*/

$SiteUrl = (empty($_POST['SiteUrl']))?"":$_POST['SiteUrl'];
$WebType = (empty($_POST['WebType']))?"Chrome":$_POST['WebType'];	// "Chrome" or "Firefox" or "curl"
$Referer = (empty($_POST['Referer']))?"":$_POST['Referer'];
$Agent = (empty($_POST['Agent']))?"":$_POST['Agent'];
$Proxy = (empty($_POST['Proxy']))?"":$_POST['Proxy'];



if($SiteUrl == "") {
	$PageHtml = "SiteUrl Error";
} else {

	
	if($WebType == "phpcurl"){
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
		$RunData = array();
		$RunData['SiteUrl'] = $SiteUrl;
		$RunData['WebType'] = $WebType;
		$RunData['Referer'] = $Referer;
		$RunData['Agent'] = $Agent;
		$RunData['Proxy'] = $Proxy;

		$MConfigData = escapeshellarg(json_encode($RunData));

		exec("python3 /home/ntosmini/public_html/NtosMini/_WebScrap_ub_ali.py {$MConfigData}", $ResultArr);
		$PageHtml = implode("\n", $ResultArr);
	}	//end if


	if($PageHtml){
		$PageHtml = $PageHtml;
	} else {
		$PageHtml = "PageHtml Error";
	}	//end if
}	//end if SiteUrl

echo base64_encode($PageHtml);

