from urllib import request
from bs4 import BeautifulSoup

url = 'http://www.cgv.co.kr/movies/'
response = request.urlopen(url)
soup = BeautifulSoup(response,'html.parser') #구조화
print(soup)

result = soup.select('strong.title')
print(result)

for item in result:
    print(item.string)



# div태그: 구분용, 줄 안 바꿈
# strong: 진하게 
# span태그: 구분용, 줄 바꿈
# li태그 :리스트 만듦