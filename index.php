<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");
/*
셀레니움 실행 확인용
*/
$Type = (empty($_GET['Type']))?"":$_GET['Type'];

$RunData = array();
$RunData['StartUrl'] = (empty($_GET['StartUrl']))?"":urldecode($_GET['StartUrl']);
$RunData['SiteUrl'] = (empty($_GET['SiteUrl']))?"http://product.ntos.co.kr/_SeleniumChk.php":urldecode($_GET['SiteUrl']);
$RunData['UserAgent'] = (empty($_GET['UserAgent']))?"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36":$_GET['UserAgent'];
$RunData['CookiesLang'] = (empty($_GET['CookiesLang']))?"":$_GET['CookiesLang'];	//쿠키 언어
$MConfigData = escapeshellarg(json_encode($RunData));

if(empty($Type)){
	$PageHtml = "<div>ntoswebsuccess</div>";
	$PageHtml .= "<div>";
	$PageHtml .= "<form method='get'>";
	$PageHtml .= "<select name='Type'>";
	$PageHtml .= "<option value=''>self</option>";
	$PageHtml .= "<option value='curl'>curl</option>";
	$PageHtml .= "<option value='se'>se</option>";
	$PageHtml .= "<option value='uc'>uc</option>";
	$PageHtml .= "</select>";
	$PageHtml .= " <input type='text' name='SiteUrl' style='width:90%;'>";
	$PageHtml .= "</br><input type='submit' value=' 확 인 '>";
	$PageHtml .= "</div>";
} else if($Type == "curl"){
	exec("python3 /home/ntosmini/public_html/index.curl.py {$MConfigData}", $ResultArr);
	$PageHtml = implode("\n", $ResultArr);
} else if($Type == "se"){
	exec("python3 /home/ntosmini/public_html/index.se.py {$MConfigData}", $ResultArr);
	$PageHtml = implode("\n", $ResultArr);
} else if($Type == "uc"){
	if(empty($RunData['CookiesLang'])){
		exec("PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin python3 /home/ntosmini/public_html/index.uc.py {$MConfigData}", $ResultArr);
	} else {
		exec("PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin python3 /home/ntosmini/public_html/index.uc.Cookies.py {$MConfigData}", $ResultArr);
	}
	$PageHtml = implode("\n", $ResultArr);
		
} else {
	$PageHtml = "error : Type";
}
echo $PageHtml;
