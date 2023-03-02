from urllib import request

url = 'https://kukka-2-media-123.s3.amazonaws.com/media/catalog/product/detail/8bcd5337-c566-4cd2-96e5-848e2db0968f.jpg'
filename = '05_crawling/down/프리지아.jpg' #이미지가 천 장 필요, 구글에서 검색하고 img태그 찾아서 src가져오면 주소 나옴 for문 돌라면 됨, 오류 방지 위해 try-except 사용
request.urlretrieve(url, filename) #코드 전체면 url open, 이미지만 가져올거라 #해당 파일 그대로 내려 받는 것
