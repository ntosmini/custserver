<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");

$RunData = array();
$ScrapType = (empty($_POST['ScrapType']))?"selenium":$_POST['ScrapType'];	//수집방식 - curl or self or selenium or pyget
$RunData['UserAgent'] = (empty($_POST['UserAgent']))?"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36":$_POST['UserAgent'];
$ChromeType = (empty($_POST['ChromeType']))?"":$_POST['ChromeType'];
$RunData['ChromeVer'] = (empty($_POST['ChromeVer']))?"":$_POST['ChromeVer'];	//Chrome version
if($ScrapType == "self"){

	echo "ntoswebsuccess";
	exit;

} else if($ScrapType == "curl") {

	$SiteUrlOne = (empty($_POST['SiteUrlOne']))?"":$_POST['SiteUrlOne'];
	$Agent = (empty($_POST['Agent']))?"":$_POST['Agent'];

	if(empty($SiteUrlOne)){
		echo 'not SiteUrlOne';
		exit;
	}
	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, $SiteUrlOne);
	curl_setopt($ch, CURLOPT_HEADER, false);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
	curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
	curl_setopt($ch, CURLOPT_AUTOREFERER, true);
	
	$Agent = (empty($Agent))?"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36":$Agent;
	curl_setopt($ch, CURLOPT_USERAGENT, $Agent);
	curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 60); //
	curl_setopt($ch, CURLOPT_TIMEOUT, 120); //
	$PageHtml=curl_exec($ch);
	$http_code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
	curl_close($ch);

	echo $http_code."|@|".$PageHtml;
	exit;

} else if($ScrapType == "selenium") {
	$RunData['CustId'] = (empty($_POST['CustId']))?"":$_POST['CustId'];
	if(empty($RunData['CustId'])){
		echo 'not CustId';
		exit;
	}
	$RunData['StartSiteUrl'] = (empty($_POST['StartSiteUrl']))?"":$_POST['StartSiteUrl'];	//시작 url
	$RunData['SiteUrlOne'] = (empty($_POST['SiteUrlOne']))?"N":$_POST['SiteUrlOne'];
	$RunData['SiteUrl_SaveFileName'] = (empty($_POST['SiteUrl_SaveFileName']))?"":$_POST['SiteUrl_SaveFileName'];	//수집url|@|저장파일명 or N -- 
	$RunData['Refresh'] = ($_POST['Refresh'] == "Y")?$_POST['Refresh']:"N";;	//새로고침 - Y or N
	$RunData['Scroll'] = ($_POST['Scroll'] == "Y")?$_POST['Scroll']:"N";	//스크롤 내리기 - Y or N
	$RunData['ScrapResultType'] = (empty($_POST['ScrapResultType']))?"view":$_POST['ScrapResultType'];	//수집파일 방식 - save or send or view

	if($RunData['SiteUrlOne'] == "N" && $RunData['ScrapResultType'] == "view"){
		echo "not SiteUrlOne : ".$RunData['SiteUrlOne'].", ScrapResultType : ".$RunData['ScrapResultType'];
		exit;
	}
	/*
	저장 폴더
	/home/ntosmini/ali_item_en/
	/home/ntosmini/ali_item_kr/
	/home/ntosmini/ali_category/

	/home/ntosmini/scrapdata/
	*/
	$RunData['FileSaveDir'] = (($RunData['ScrapResultType'] == "save" || $RunData['ScrapResultType'] == "send") && $_POST['FileSaveDir'])?$_POST['FileSaveDir']:"";
	if(empty($RunData['FileSaveDir']) && ($RunData['ScrapResultType'] == "save" || $RunData['ScrapResultType'] == "send")){
		echo "not FileSaveDir (".$RunData['ScrapResultType'].")";
		exit;
	}
	
	$RunData['NtosSendServer'] = ($RunData['ScrapResultType'] == "send" && $_POST['NtosSendServer'])?$_POST['NtosSendServer']:"";	//전송서버 폴더까지
	if(empty($RunData['NtosSendServer']) && $RunData['ScrapResultType'] == "send"){
		echo "not NtosSendServer (".$RunData['ScrapResultType'].")";
		exit;
	}

	$RunData['SiteUrl_SaveFileName'] = explode("|^|", $RunData['SiteUrl_SaveFileName']);

	$MConfigData = escapeshellarg(json_encode($RunData));
	if($ChromeType == "uc"){
		exec("PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin python3 /home/ntosmini/public_html/_Scrap_/Scrap.uc.py {$MConfigData}", $ResultArr);		
	} else {
		exec("python3 /home/ntosmini/public_html/_Scrap_/Scrap.py {$MConfigData}", $ResultArr);
	}

	$PageHtml = implode("\n", $ResultArr);

	echo $PageHtml;
	exit;
} else if($ScrapType == "pyget") {
	
	$RunData['CustId'] = (empty($_POST['CustId']))?"":$_POST['CustId'];
	if(empty($RunData['CustId'])){
		echo 'not CustId';
		exit;
	}
	$RunData['StartSiteUrl'] = (empty($_POST['StartSiteUrl']))?"":$_POST['StartSiteUrl'];	//시작 url
	$RunData['SiteUrlOne'] = (empty($_POST['SiteUrlOne']))?"N":$_POST['SiteUrlOne'];
	$RunData['SiteUrl_SaveFileName'] = (empty($_POST['SiteUrl_SaveFileName']))?"":$_POST['SiteUrl_SaveFileName'];	//수집url|@|저장파일명 or N -- 
	$RunData['Refresh'] = ($_POST['Refresh'] == "Y")?$_POST['Refresh']:"N";;	//새로고침 - Y or N
	$RunData['Scroll'] = ($_POST['Scroll'] == "Y")?$_POST['Scroll']:"N";	//스크롤 내리기 - Y or N
	$RunData['ScrapResultType'] = (empty($_POST['ScrapResultType']))?"view":$_POST['ScrapResultType'];	//수집파일 방식 - save or send or view

	if($RunData['SiteUrlOne'] == "N" && $RunData['ScrapResultType'] == "view"){
		echo "not SiteUrlOne : ".$RunData['SiteUrlOne'].", ScrapResultType : ".$RunData['ScrapResultType'];
		exit;
	}
	$RunData['NtosSendServer'] = ($RunData['ScrapResultType'] == "send" && $_POST['NtosSendServer'])?$_POST['NtosSendServer']:"";	//전송서버 폴더까지
	/*
	저장 폴더
	/home/ntosmini/ali_item_en/
	/home/ntosmini/ali_item_kr/
	/home/ntosmini/ali_category/

	/home/ntosmini/scrapdata/
	*/
	$RunData['FileSaveDir'] = (($RunData['ScrapResultType'] == "save" || $RunData['ScrapResultType'] == "send") && $_POST['FileSaveDir'])?$_POST['FileSaveDir']:"";
	
	
	$RunData['SiteUrlOne'] = (empty($_POST['SiteUrlOne']))?"N":$_POST['SiteUrlOne'];
	$RunData['ScrapResultType'] = (empty($_POST['ScrapResultType']))?"view":$_POST['ScrapResultType'];	//수집파일 방식 - save or send or view
	if($RunData['SiteUrlOne'] == "N"){
		echo "not SiteUrlOne";
		exit;
	}
	$MConfigData = escapeshellarg(json_encode($RunData));
	if($ChromeType == "uc"){
		exec("PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin python3 /home/ntosmini/public_html/_Scrap_/Scrap.uc.py {$MConfigData}", $ResultArr);		
	} else {
		exec("python3 /home/ntosmini/public_html/_Scrap_/Scrap.py {$MConfigData}", $ResultArr);
	}

	$PageHtml = implode("\n", $ResultArr);

	echo $PageHtml;
	exit;
	
} else {
	echo 'not ScrapType';
	exit;
}







/*
$ScrapType = (empty($_POST['ScrapType']))?"selenium":$_POST['ScrapType'];	//수집방식 - curl or self or selenium


$ScrapType == "self"


$ScrapType == "curl"
$_POST['SiteUrlOne']
$_POST['Agent']
echo $http_code."|@|".$PageHtml;

$ScrapType == "selenium"
$RunData['CustId'] = (empty($_POST['CustId']))?"":$_POST['CustId'];
$RunData['StartSiteUrl'] = (empty($_POST['StartSiteUrl']))?"":$_POST['StartSiteUrl'];	//시작 url
$RunData['SiteUrlOne'] = (empty($_POST['SiteUrlOne']))?"":$_POST['SiteUrlOne'];
$RunData['SiteUrl_SaveFileName'] = (empty($_POST['SiteUrl_SaveFileName']))?"":$_POST['SiteUrl_SaveFileName'];	//수집url|@|저장파일명 or N -- 
$RunData['Scroll'] = ($_POST['Scroll'] == "Y")?$_POST['Scroll']:"N";	//스크롤 내리기 - Y or N
$RunData['Refresh'] = ($_POST['Refresh'] == "Y")?$_POST['Refresh']:"N";;	//새로고침 - Y or N
$RunData['ScrapResultType'] = (empty($_POST['ScrapResultType']))?"view":$_POST['ScrapResultType'];	//수집파일 방식 - save or send or view
$RunData['FileSaveDir'] = ($RunData['ScrapResultType'] == "save" && $RunData['FileSaveDir'])?$RunData['FileSaveDir']:"";
$RunData['NtosSendServer'] = ($RunData['ScrapResultType'] == "send" && $RunData['NtosSendServer'])?$RunData['NtosSendServer']:"";	//전송서버 폴더까지
*/
