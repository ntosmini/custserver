<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");

$RunData = array();
$RunData['NtosServer'] = (empty($_POST['NtosServer']))?"":$_POST['NtosServer'];
$RunData['CustId'] = (empty($_POST['CustId']))?"":$_POST['CustId'];
$RunData['it_id'] = (empty($_POST['it_id']))?"":$_POST['it_id'];
$RunData['TransStr'] = (empty($_POST['TransStr']))?"":$_POST['TransStr'];
$RunData['OrgField'] = (empty($_POST['OrgField']))?"":$_POST['OrgField'];
$RunData['TargetField'] = (empty($_POST['TargetField']))?"":$_POST['TargetField'];
$RunData['g_dest'] = (empty($_POST['g_dest']))?"":$_POST['g_dest']; //번역
$RunData['g_src'] = (empty($_POST['g_src']))?"":$_POST['g_src'];  //원문

if(
empty($RunData['NtosServer'])
|| empty($RunData['CustId'])
|| empty($RunData['it_id'])
|| empty($RunData['TransStr'])
|| empty($RunData['OrgField'])
|| empty($RunData['TargetField'])
|| empty($RunData['g_dest'])
|| empty($RunData['g_src'])
){
	echo "Not Data";
  exit;
}

$MConfigData = escapeshellarg(json_encode($RunData));

exec("python3 /home/ntosmini/public_html/_Trans_/trans.py {$MConfigData}", $ResultArr);

$PageHtml = implode("\n", $ResultArr);

echo $PageHtml;
