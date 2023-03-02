from urllib import request


url = 'https://www.naver.com/'
result = request.urlopen(url).read()  #리드 전까지는 개체 #리드 후 읽어 줌
print(type(result)) #네트워크-서버/ 웹브라우저 상에서 서버로 요청이 들어가면 필요한 정보들이 리퀘스트라는 개체로 만들어져 서버에서 리스펀스 개체 만듦 웹으로 보내 해석해 네이버 처음 창처럼 보이게 함
print(result.decode('utf-8')) #</html>\n' 줄바꿈, 문자열로 #.decode('utf-8') 한글로 바꿈
