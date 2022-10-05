<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");


$SiteUrl = (empty($_POST['SiteUrl']))?"not":$_POST['SiteUrl'];
$WebType = (empty($_POST['WebType']))?"Chrome":$_POST['WebType'];	// "Chrome" or "Firefox" or "curl"
$Referer = (empty($_POST['Referer']))?"not":$_POST['Referer'];

if($SiteUrl == "not") {
	$PageHtml = "Error";
} else {

if($WebType == "curl"){
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $SiteUrl );
    curl_setopt($ch, CURLOPT_HEADER, false);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
	$Agent = ($Agent == "not")?"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36":$Agent;
	curl_setopt($ch, CURLOPT_USERAGENT, $_SERVER['HTTP_USER_AGENT']);
	curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 120); //
	curl_setopt($ch, CURLOPT_TIMEOUT, 300); //
    $ret=curl_exec($ch);
    curl_close($ch);
	$PageHtml = $ret;
} else {
	$SiteUrl = base64_encode($SiteUrl);
	$Referer = base64_encode($Referer);

	ob_start();
	passthru(dirname(__FILE__)."/_WebScrap.py $SiteUrl $WebType $Referer");
	$PageHtml = ob_get_clean(); 
	ob_end_clean();
}	//end if

	if($PageHtml){
		$PageHtml = $PageHtml;
	} else {
		$PageHtml = "Error";
	}	//end if
}	//end if SiteUrl
echo base64_encode($PageHtml);
