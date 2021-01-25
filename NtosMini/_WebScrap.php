<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");


$SiteUrl = (empty($_POST['SiteUrl']))?"not":$_POST['SiteUrl'];
$WebType = (empty($_POST['WebType']))?"Chrome":$_POST['WebType'];	// "Chrome" or "Firefox" or "curl"
$Referer = (empty($_POST['Referer']))?"not":$_POST['Referer'];

if($SiteUrl == "not") {
	$PageHtml = "Error";
} else {


	$SiteUrl = base64_encode($SiteUrl);
	$Referer = base64_encode($Referer);

	ob_start();
	passthru(dirname(__FILE__)."/_WebScrap.py $SiteUrl $WebType $Referer");
	$PageHtml = ob_get_clean(); 
	ob_end_clean();

	if($PageHtml){
		$PageHtml = $PageHtml;
	} else {
		$PageHtml = "Error";
	}	//end if
}	//end if SiteUrl
echo base64_encode($PageHtml);