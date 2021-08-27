#@langkhach
#date 210827
import re
from mitmproxy import http, proxy, options

regexes_block = [
    '^https?:\/\/.+.googlevideo.com\/ptracking\?pltype=adhost',
    '^https?:\/\/.+.youtube.com\/api\/stats\/ads',
    '^https?:\/\/.+.youtube.com\/get_midroll_',
    '^https?:\/\/.+\.youtube\.com\/pagead',
    '^https?:\/\/.+\.youtube\.com\/ptracking',
    '^https?:\/\/.+.youtube.com\/_get_ads',
    '^https?:\/\/youtubei.googleapis.com\/.+ad_break',
    '^https?:\/\/youtubei.googleapis.com\/youtubei\/.+(ad|log)',
    '^https:\/\/youtubei\.googleapis\.com\/youtubei\/v1\/att\/get',
    '^https?:\/\/.+\.googlevideo\.com\/videogoodput',
    '^https?:\/\/.+\.googlevideo\.com\/.+owc=',
    '^https?:\/\/.+\.youtube\.com\/pagead',
    '^https?:\/\/.+\.googlevideo\.com\/.+&oad'
]
regexes_redirect = [
'^https?:\/\/.+?\.googlevideo\.com\/.+&ctier=(?!A)'
]
def url_matches(url, regexes):
    return any(re.search(regex, url) for regex in regexes)
def request(flow):
    if url_matches(flow.request.pretty_url, regexes_block):
        print("Matched request block: ", flow.request.pretty_url)         
        flow.response = http.HTTPResponse.make(
                200,
                b"",
                {"Content-Type": "text/html"}
            )
    if url_matches(flow.request.pretty_url, regexes_redirect):
        print("Matched request redirect: ", flow.request.pretty_url) 
        flow.request.url = flow.request.url.replace("ctier=L", "ctier=A")