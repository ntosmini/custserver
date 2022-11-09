<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");
/*
카테고리 - 스트레이트
*/
$RunData = array();
$Ver = (empty($_POST['Ver']))?"v3":$_POST['Ver'];	//v3 or v4
$RunData['NtosServer'] = (empty($_POST['NtosServer']))?"":$_POST['NtosServer'];
$RunData['CslId_SiteUrl'] = (empty($_POST['CslId_SiteUrl']))?"":$_POST['CslId_SiteUrl'];
$RunData['Agent'] = (empty($_POST['Agent']))?"":$_POST['Agent'];
$RunData['NotsKey'] = (empty($_POST['NotsKey']))?"":$_POST['NotsKey'];
$RunData['CustId'] = (empty($_POST['CustId']))?"":$_POST['CustId'];
$RunData['Scroll'] = (empty($_POST['Scroll']))?"N":$_POST['Scroll'];
$RunData['TimeChk'] = (empty($_POST['TimeChk']))?"N":$_POST['TimeChk'];



if(empty($RunData['NtosServer']) || empty($RunData['CslId_SiteUrl']) || empty($RunData['CustId']) || empty($RunData['NotsKey'])){
	echo 'error';
	exit;
}	//end if

$MConfigData = escapeshellarg(json_encode($RunData));

exec("python3 /home/ntosmini/public_html/_NtosSc_/ali/_CategoryStraight.{$Ver}.py {$MConfigData}", $ResultArr);
$PageHtml = implode("\n", $ResultArr);

echo $PageHtml;