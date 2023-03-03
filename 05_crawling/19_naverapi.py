# 네이버 검색 API 예제 - 블로그 검색
   
import urllib.request
import json

client_id = "아이디"
client_secret = "비번"
query = input('오타변환 >>> ')
encText = urllib.parse.quote(query)
url = "https://openapi.naver.com/v1/search/errata.json?query=" + encText # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
    
data = response_body.decode('utf-8')
print(type(data))
result = json.loads(data)
print(result)
