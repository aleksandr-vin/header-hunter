

copy_as_curl = {
    'safari': {
        'Version 17.0 (19616.1.27.211.1)': """curl 'https://somewhere.nl/my-account/profile/index.html' \
-X 'GET' \
-H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' \
-H 'Sec-Fetch-Site: same-origin' \
-H 'Cookie: MpConsentState=AdobeAudienceManager,Google,Facebook,Criteo,GoogleAnalytics; XXSession=xxxxxx-xxxx-xxxx-xxxx-xxxxxxxx; cs_fpid=xxxxxxyyyyyy; fffff=bbbbb' \
-H 'Sec-Fetch-Dest: document' \
-H 'Accept-Language: en-GB,en;q=0.9' \
-H 'Sec-Fetch-Mode: navigate' \
-H 'Host: somewhere.nl' \
-H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15' \
-H 'Referer: https://somewhere.nl/' \
-H 'Accept-Encoding: gzip, deflate, br' \
-H 'Connection: keep-alive'"""
    }
}