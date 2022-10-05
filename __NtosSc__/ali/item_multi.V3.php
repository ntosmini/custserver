<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");
/*
알리 카테고리 - 멀티
*/

$RunData = array();
$RunData['NtosServer'] = (empty($_POST['NtosServer']))?"":$_POST['NtosServer'];
$RunData['SlId_SiteUrl_Proxy'] = (empty($_POST['SlId_SiteUrl_Proxy']))?"":$_POST['SlId_SiteUrl_Proxy'];
$RunData['NotsKey'] = (empty($_POST['NotsKey']))?"":$_POST['NotsKey'];
$RunData['CustId'] = (empty($_POST['CustId']))?"":$_POST['CustId'];


if(empty($RunData['NtosServer']) || empty($RunData['SlId_SiteUrl_Proxy']) || empty($RunData['CustId']) || empty($RunData['NotsKey'])){
	echo 'error';
	exit;
}	//end if



$MConfigData = escapeshellarg(json_encode($RunData));


exec("python3 /home/ntosmini/public_html/__NtosSc__/ali/item_multi.V3.py {$MConfigData}", $ResultArr);
$PageHtml = implode("\n", $ResultArr);

echo $PageHtml;
