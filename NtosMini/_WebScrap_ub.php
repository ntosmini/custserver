<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");


$SiteUrl = (empty($_POST['SiteUrl']))?"not":$_POST['SiteUrl'];
$WebType = (empty($_POST['WebType']))?"Chrome":$_POST['WebType'];	// "Chrome" or "Firefox" or "curl"
$Referer = (empty($_POST['Referer']))?"not":$_POST['Referer'];
$Agent = (empty($_POST['Agent']))?"not":$_POST['Agent'];
$Proxy = (empty($_POST['Proxy']))?"not":$_POST['Proxy'];


if($SiteUrl == "not") {
	$PageHtml = "SiteUrl Error";
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
	$Agent = base64_encode($Agent);

	ob_start();
	passthru("python3 /home/ntosmini/public_html/NtosMini/_WebScrap_ub.py $SiteUrl $WebType $Referer $Agent $Proxy");
	$PageHtml = ob_get_clean(); 

}	//end if


	if($PageHtml){
		$PageHtml = $PageHtml;
	} else {
		$PageHtml = "PageHtml Error";
	}	//end if
}	//end if SiteUrl
echo base64_encode($PageHtml);