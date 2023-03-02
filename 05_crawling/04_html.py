# https://search.naver.com/search.naver?where=nexearch&sm=tab_jum&query=%EB%B2%9A%EA%BD%83%EC%B6%95%EC%A0%9C #?부터 쿼리스트링, &는 ,
# get방식으로 요청하는 것이 기본, url에 데이터 들어가 있음 눈으로 확인 가능 /post방식 데이터를 넣어 가기에 눈으로 확인 불가

from urllib import request,parse
query = input('검색할 키 >>> ')
api = 'https://search.naver.com/search.naver?'
values = {
# 'where' : 'nexearch',
'query': query,
# 'oquery':'벚꽃',
# 'sm':'tab_jum',
# 'query':'%EB%B2%9A%EA%BD%83%EC%B6%95%EC%A0%9C', # %와 16진수로 한글 표현
# 'acq':'벚꽃'
# 'acr':4,
# 'qdt':0
}

params = parse.urlencode(values) #urlencode 위에 한글을 전환해 주는 것
print(params)
url = api + params
print(url)

result = request.urlopen(url).read().decode('utf8')
print(result)