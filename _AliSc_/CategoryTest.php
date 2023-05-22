<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");
/*
카테고리 - 스트레이트
*/
$RunData = array();
$Ver = "v4";

$RunData['CslId_SiteUrl'][] = "https://ko.aliexpress.com/category/100001184/nail-tables.html?shipFromCountry=CN&dida=y?shipFromCountry=CN&minPrice=910001&maxPrice=930000&SortType=price_desc&page=2|@|ali03.ntos.co.kr_cate_aliexpress_2967598_004005005011000_2_201_7061837.html";
$RunData['CslId_SiteUrl'][] = "https://ko.aliexpress.com/category/100001184/nail-tables.html?shipFromCountry=CN&dida=y?shipFromCountry=CN&minPrice=84001&maxPrice=87000&SortType=price_desc&page=2|@|ali03.ntos.co.kr_cate_aliexpress_2967658_004005005011000_2_201_7061838.html";
$RunData['CslId_SiteUrl'][] = "https://ko.aliexpress.com/category/200217311/pedicure-chairs.html?shipFromCountry=CN&dida=y?shipFromCountry=CN&minPrice=1370001&maxPrice=1390000&SortType=price_desc&page=2|@|ali03.ntos.co.kr_cate_aliexpress_2967718_004005005011000_2_201_7061839.html";
$RunData['CslId_SiteUrl'][] = "https://ko.aliexpress.com/category/200217311/pedicure-chairs.html?shipFromCountry=CN&dida=y?shipFromCountry=CN&minPrice=170001&maxPrice=190000&SortType=price_desc&page=2|@|ali03.ntos.co.kr_cate_aliexpress_2967778_004005005011000_2_201_7061840.html";
$RunData['CslId_SiteUrl'][] = "https://ko.aliexpress.com/category/100001181/shampoo-chairs.html?shipFromCountry=CN&dida=y?shipFromCountry=CN&minPrice=1830001&maxPrice=1850000&SortType=price_desc&page=2|@|ali03.ntos.co.kr_cate_aliexpress_2967838_004005005011000_2_201_7061841.html";

$RunData['CustId'] = "aliexpress";
$RunData['Scroll'] = "N";	//스크롤

$RunData['FileSendSave'] = "N";	//파일 저장 전송 사용여부 Y/N
$RunData['NtosServer'] = "http://ali03.ntos.co.kr/_AliWb_/ScrapSaveFile.php";	//받을 url
$RunData['UserAgent'] = (empty($_POST['UserAgent']))?"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36":$_POST['UserAgent'];

if(empty($Ver) || ($Ver != 'v3' && $Ver != 'v4') ){
	echo 'not Ver';
	exit;
}	//end if(empty($Ver))

if(empty($RunData['CslId_SiteUrl'])){
	echo 'not CslId_SiteUrl';
	exit;
}
$RunData['CslId_SiteUrl'] = explode("|^|", $RunData['CslId_SiteUrl']);

if(empty($RunData['CustId'])){
	echo 'not CustId';
	exit;
}

$MConfigData = escapeshellarg(json_encode($RunData));


exec("python3 /home/ntosmini/public_html/_AliSc_/Category.{$Ver}.py {$MConfigData}", $ResultArr);

$PageHtml = implode("\n", $ResultArr);

echo $PageHtml;
