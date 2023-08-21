<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");

$RunData = array();
$ScrapType = (empty($_POST['ScrapType']))?"uc":$_POST['ScrapType'];	//수집방식 - curl or self or selenium or pyget
$RunData['SiteUrl'] = (empty($_POST['SiteUrl']))?"":$_POST['SiteUrl'];

$RunData['CustId'] = (empty($_POST['CustId']))?"":$_POST['CustId'];
$RunData['FileSendSave'] = (empty($_POST['FileSendSave']))?"n":$_POST['FileSendSave'];	//파일 저장 전송 사용여부 y/n
$RunData['NtosServer'] = (empty($_POST['NtosServer']))?"":$_POST['NtosServer'];	//받을 url
$RunData['FileDir'] = (empty($_POST['FileDir']))?"":$_POST['FileDir'];	//xs 서버 저장 폴더

if(empty($RunData['SiteUrl'])){
	echo 'not SiteUrl';
	exit;
}

switch($ScrapType){
	case 'uc' :
		exec("PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin python3 /home/ntosmini/public_html/_Scrap_/Scrap.uc.py {$MConfigData}", $ResultArr);
	break;

	default :
		echo "ntoswebsuccess";
		exit;
	break;
}
$PageHtml = implode("\n", $ResultArr);
echo $PageHtml;
exit;
