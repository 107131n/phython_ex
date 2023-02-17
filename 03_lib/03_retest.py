import re

data = """
park 800905-1049118
kim  700905-1059119
"""

# pat = re.compile("(\d{6})[-]\d{7}") #찾고자 하는 패턴 #{n}:n회 반복 #():그룹 묶을 때 #[]:한 자리에 들어갈 문자
# print(pat.sub("\g<1>-*******",data)) #패턴.sub = 찾아 바꾸기

# p = re.compile('ab*')
# print(p.match('cabb'))
# print(p.search('cab'))
# p = re.compile('[a-z]+')
# print(p.match('1asxr한'))
# print(p.search('1asxr한'))
# result = p.search('1asxr한')
# print(result)
# print(result.start())
# print(result.end())
# print(result.span())
# print(result.group())
# print(result.groups())

p = re.compile('[0-9]{6}[-][1-4][0-9]{6}')
result = p.findall(data) 
print(result) 
for r in result : print(r)

#findall: 리스트로 리턴 #finditer: 객체로 리턴