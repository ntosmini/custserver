<?php
set_time_limit(0);
header("Content-Type: text/html; charset=UTF-8");
/*
2022-03-21
*/

$SiteUrl = (empty($_POST['SiteUrl']))?"not":$_POST['SiteUrl'];
$WebType = (empty($_POST['WebType']))?"Chrome":$_POST['WebType'];	// "Chrome" or "Firefox" or "curl"
$Referer = (empty($_POST['Referer']))?"not":$_POST['Referer'];
$Agent = (empty($_POST['Agent']))?"not":$_POST['Agent'];
$Proxy = (empty($_POST['Proxy']))?"not":$_POST['Proxy'];


if($SiteUrl == "not") {
	$PageHtml = "SiteUrl Error";
} else {

	
	if($WebType == "phpcurl"){

// redirect 처리 필요.
function curl_get_follow_url(/*resource*/ $ch, /*int*/ &$maxredirect = null) {
    $mr = $maxredirect === null ? 5 : intval($maxredirect);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, false);
    if ($mr > 0) {
        $newurl = curl_getinfo($ch, CURLINFO_EFFECTIVE_URL);

        $rch = curl_copy_handle($ch);
        curl_setopt($rch, CURLOPT_HEADER, true);
        curl_setopt($rch, CURLOPT_NOBODY, true);
        curl_setopt($rch, CURLOPT_FORBID_REUSE, false);
        curl_setopt($rch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($rch, CURLOPT_CONNECTTIMEOUT, 2); 
        curl_setopt($rch, CURLOPT_TIMEOUT, 3); 
        do {
            curl_setopt($rch, CURLOPT_URL, $newurl);
            $header = curl_exec($rch);
            if (curl_errno($rch)) {
                $code = 0;
            } else {
                $code = curl_getinfo($rch, CURLINFO_HTTP_CODE);
                if ($code == 301 || $code == 302) {
                    preg_match('/Location:(.*?)\n/', $header, $matches);
                    $newurl = trim(array_pop($matches));
                } else {
                    $code = 0;
                }
            }
        } while ($code && --$mr);
        curl_close($rch);
        if (!$mr) {
            if ($maxredirect === null) {
                trigger_error('Too many redirects. When following redirects, libcurl hit the maximum amount.', E_USER_WARNING);
            } else {
                $maxredirect = 0;
            }
            return false;
        }
    }
    return $newurl;
}
		
		$ch = curl_init();
		curl_setopt($ch, CURLOPT_URL, $SiteUrl );
		curl_setopt($ch, CURLOPT_HEADER, false);
		curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
		//curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
		curl_setopt($ch, CURLOPT_AUTOREFERER, true);
		
		$Agent = ($Agent == "not")?"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36":$Agent;
		curl_setopt($ch, CURLOPT_USERAGENT, $Agent);


		if( ini_get('open_basedir') == '' && ini_get('safe_mode') == 'Off' ){
			curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true); // URL 이 바뀌는 경우. 304 move ..
			curl_setopt($ch, CURLOPT_MAXREDIRS, 2); // 너무 많지 않게.
		}else{
			// get url.
			$new_url = curl_get_follow_url($ch);
			curl_close($ch);
			$ch = curl_init($new_url); // image path.
		}




		curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 120); //
		curl_setopt($ch, CURLOPT_TIMEOUT, 300); //
		$PageHtml=curl_exec($ch);
		curl_close($ch);



	} else {
		$SiteUrl = base64_encode($SiteUrl);
		$Referer = base64_encode($Referer);
		$Agent = base64_encode($Agent);

		ob_start();
		passthru("python3 /home/ntosmini/public_html/NtosMini/_WebScrap_ub.py $SiteUrl $WebType $Referer $Agent $Proxy");
		$PageHtml = ob_get_clean(); 
	}	//end if


	if($PageHtml){
		$PageHtml = $PageHtml;
	} else {
		$PageHtml = "PageHtml Error";
	}	//end if
}	//end if SiteUrl
echo base64_encode($PageHtml);
