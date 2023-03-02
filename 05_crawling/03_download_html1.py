import requests

# r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass')) #아무 말 없으면 get
# print(r.status_code) #200은 성공
# print(r.headers['content-type'])
# print(r.encoding)
# print(r.text) #글자도 text하면 끝
# print(r.json()) #json 문자열을 json으로 읽으려면 loads(파일은 load)

r = requests.get('https://www.naver.com')
print(r.status_code) 
print(r.headers['content-type'])
print(r.encoding) # text/html; charset=UTF-8
# print(r.text) 
# print(r.json()) 

