<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");
/*
셀레니움 실행 확인용
*/
$Type = (empty($_GET['Type']))?"":$_GET['Type'];
$Ver = (empty($_GET['Ver']))?"v4":$_GET['Ver'];


if(empty($Type)){
	$PageHtml = "success";
} else if($Type == "py"){
	if($Ver == "v4" || $Ver == "v3"){
		exec("python3 /home/ntosmini/public_html/__NtosSc__/_test.{$Ver}.py", $ResultArr);
		$PageHtml = implode("\n", $ResultArr);
	} else {
		$PageHtml = "error : Not Ver";
	}
} else {
	$PageHtml = "error : Type";
}
echo $PageHtml;