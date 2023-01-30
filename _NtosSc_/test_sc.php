<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");
/*
Scrap
*/

$RunData = array();
$Ver = (empty($_POST['Ver']))?"v4":$_POST['Ver'];	//v3 or v4
$RunData['RunSiteUrl'] = "http://ntos.co.kr|@|1_001001019000000_61_.html";
$RunData['CustId'] = "banggood";
$RunData['ScrapType'] = "cate";

$RunData['Scroll'] = "N";
$RunData['Refresh'] = "N";

$RunData['FileSaveDir'] = "/home/ntosmini/scrapdata/";
$RunData['FileSave'] = "Y";
$RunData['NtosServer'] = "http://product.ntos.co.kr/_NtosWb_/_FileSave.php";





if(empty($Ver) || ($Ver != 'v3' && $Ver != 'v4') ){
	echo 'not Ver';
	exit;
}	//end if(empty($Ver))

if(empty($RunData['RunSiteUrl'])){
	echo 'not RunSiteUrl';
	exit;
}
$RunData['RunSiteUrl'] = explode("|^|", $RunData['RunSiteUrl']);

if(empty($RunData['CustId'])){
	echo 'not CustId';
	exit;
}

if(empty($RunData['ScrapType'])){
	echo 'not ScrapType';
	exit;
}

$MConfigData = escapeshellarg(json_encode($RunData));

echo "/home/ntosmini/public_html/_NtosSc_/Scrap.{$Ver}.py";
exec("python3 /home/ntosmini/public_html/_NtosSc_/ScrapSend.{$Ver}.py {$MConfigData}", $ResultArr);

$PageHtml = implode("\n", $ResultArr);

echo $PageHtml;
