<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");
/*
상품 - 스트레이트
*/

$RunData = array();
$Ver = (empty($_POST['Ver']))?"v3":$_POST['Ver'];	//v3 or v4
$RunData['NtosServer'] = (empty($_POST['NtosServer']))?"":$_POST['NtosServer'];
$RunData['IslId_SiteUrl'] = (empty($_POST['IslId_SiteUrl']))?"":$_POST['IslId_SiteUrl'];
$RunData['NotsKey'] = (empty($_POST['NotsKey']))?"":$_POST['NotsKey'];
$RunData['CustId'] = (empty($_POST['CustId']))?"":$_POST['CustId'];
$RunData['TimeChk'] = (empty($_POST['TimeChk']))?"N":$_POST['TimeChk'];
$RunData['LogChkUrl'] = (empty($_POST['LogChkUrl']))?"":$_POST['LogChkUrl'];
$RunData['WaitChk'] = (empty($_POST['WaitChk']))?"":$_POST['WaitChk'];
$RunData['chk_idx'] = (empty($_POST['chk_idx']))?"":$_POST['chk_idx'];


if(empty($RunData['NtosServer']) || empty($RunData['IslId_SiteUrl']) || empty($RunData['CustId']) || empty($RunData['NotsKey'])){
	echo 'error';
	exit;
}	//end if

$MConfigData = escapeshellarg(json_encode($RunData));


exec("python3 /home/ntosmini/public_html/_NtosSc_/ali/_ItemStraight.{$Ver}.py {$MConfigData}", $ResultArr);
$PageHtml = implode("\n", $ResultArr);

echo $PageHtml;
