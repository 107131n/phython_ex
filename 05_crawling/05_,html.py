import requests

query = input('검색할 키 >>> ')
api = 'https://search.naver.com/search.naver'
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

r = requests.get(api, params=values)
print(r.text) #request, urllib-request 상황에 따라 사용 