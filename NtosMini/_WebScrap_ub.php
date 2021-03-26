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

	$SiteUrl = base64_encode($SiteUrl);
	$Referer = base64_encode($Referer);
	$Agent = base64_encode($Agent);
	$WebType = "curl";
	ob_start();
	passthru("python3 /home/ntosmini/public_html/NtosMini/_WebScrap_ub.py $SiteUrl $WebType $Referer $Agent $Proxy");
	$PageHtml = ob_get_clean(); 



	if($PageHtml){
		$PageHtml = $PageHtml;
	} else {
		$PageHtml = "PageHtml Error";
	}	//end if
}	//end if SiteUrl
echo base64_encode($PageHtml);
