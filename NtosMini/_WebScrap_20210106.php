<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");
/*
스크랩


- 셀레니움 설치
pip install selenium

- BeautifulSoup 설치
pip install beautifulsoup4



*/

function CF_GetDataURL($Url, $add_opt = ''){
	global $MiniServerGet;

	if(empty($Url)) return;
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $Url );
    curl_setopt($ch, CURLOPT_HEADER, false);
    //curl_setopt($ch, CURLOPT_HTTPHEADER, array("Content-type: text/xml;charset=UTF-8"));
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

	

    // is post type ------------------------------------------------

    if( !empty($add_opt) && $add_opt['CURLOPT_FOLLOWLOCATION'] == true ){
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true); // true / false => LOCATION 등의 처리가 가능한가?
    }

    if( !empty($MiniServerGet)){

		curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($MiniServerGet));
    }


    // is post type ------------------------------------------------
    if( !empty($add_opt) && $add_opt['CURLOPT_REFERER'] != '' ){
        curl_setopt($ch, CURLOPT_REFERER, $add_opt['CURLOPT_REFERER']); 
    }

	curl_setopt($ch, CURLOPT_USERAGENT, $_SERVER['HTTP_USER_AGENT']);
	curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 120); //
	curl_setopt($ch, CURLOPT_TIMEOUT, 300); //
    $ret=curl_exec($ch);
    curl_close($ch);
    return $ret;
}// end func

$mode = (empty($_POST['mode']))?"":$_POST['mode'];
$MainUrl = (empty($_POST['MainUrl']))?"":$_POST['MainUrl'];
$MiniKey = (empty($_POST['MiniKey']))?"":$_POST['MiniKey'];
$MiniPage = (empty($_POST['MiniPage']))?"":$_POST['MiniPage'];
$it_id = (empty($_POST['it_id']))?"":$_POST['it_id'];

$SiteUrl = (empty($_POST['SiteUrl']))?"not":$_POST['SiteUrl'];
$WebType = (empty($_POST['WebType']))?"not":$_POST['WebType'];	// "Chrome" or "Firefox" or "curl"
$Referer = (empty($_POST['Referer']))?"not":$_POST['Referer'];
$brand = (empty($_POST['brand']))?"not":$_POST['brand'];

//전송값
$MiniServerGet = array();
$MiniServerGet['mode'] = $mode;
$MiniServerGet['brand'] = $brand;
$MiniServerGet['MiniKey'] = $MiniKey;
$MiniServerGet['MiniPage'] = $MiniPage;
$MiniServerGet['SiteUrl'] = $SiteUrl;
$MiniServerGet['it_id'] = $it_id;

if($MainUrl == "" || $MiniKey == "" || $MiniPage == "") {
	echo 'Error';
//	$Result = CF_GetDataURL($MainUrl);
	exit;
}


$WebType = ($WebType == "not")?"Chrome":$WebType;

$MiniServerGet['WebType'] = $WebType;
$SiteUrl = base64_encode($SiteUrl);
$Referer = base64_encode($Referer);

ob_start();
passthru("/xampp/htdocs/NtosMini/_WebScrap.py $SiteUrl $WebType $Referer");
$PageHtml = ob_get_clean(); 


if($PageHtml){
	$PageHtml = base64_encode($PageHtml);


	$MiniServerGet['code'] = 'success';
	//$MiniServerGet['status'] = 'start';
	$MiniServerGet['PageHtml'] = $PageHtml;


	$Result = json_decode(CF_GetDataURL($MainUrl), 1);
	$AddCntOrg = ($Result['AddScrap'])?count($Result['AddScrap']):0;

	if($Result['AddScrap'] && $AddCntOrg > 0){
		//$AddCnt = 1;
		foreach($Result['AddScrap'] as $Key => $Val){
			unset($Result['AddScrap'][$Key]);
			$SiteUrl = base64_encode($Val);
			ob_start();
			passthru("/xampp/htdocs/NtosMini/_WebScrap.py $SiteUrl $WebType $Referer");
			$PageHtml = ob_get_clean();
			$MiniServerGet['PageHtml'] = '';
			$MiniServerGet['AddHtml'][$Key] = base64_encode($PageHtml);
			$MiniServerGet['prod'] = $Result['prod'];
			$MiniServerGet['AddScrap'] = $Result['AddScrap'];
			//if($AddCntOrg == $AddCnt) $MiniServerGet['status'] = 'end';

			$Result = json_decode(CF_GetDataURL($MainUrl), 1);
//			print_r($Result);
			//$AddCnt++;
		}	//end foreach
	}	//end if
	ob_end_clean();


echo json_encode($Result);
	


} else {
		echo "error";
}	//end if
