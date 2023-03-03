html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p> 
"""
#html로 시작하면  html/로 끝나야 하는데, body도

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser') #(코드문자열, 파싱할 것)
# print(soup.prettify()) #prettify 보기 좋게 찍어달라는 것
# print(soup.title) #<title>The Dormouse's story</title>
# print(soup.p) # 맨 처음 만나는 p 가져옴
# print(type(soup.title)) 
# print(soup.title.name)
# print(soup.title.string) #print(soup.title.text) text라고도 함
# print(soup.p.parent.name) #body 태그 안에
# print(soup.b.parent.name) #p 태그 안에
# print(soup.p['class']) #맨 처음 p의 'class' 값
# print(soup.a['href'])
# print(soup.a['id']) #속성값에 접근할 때
# print(soup.find_all('a')) #리스트라 []로 쌓여있음, 여러 개
# print(soup.find('a')) #개체 하나라 []없이, 하나만
# print(soup.find(id='link3'))
# print(soup.find(href="http://example.com/tillie")) #find에서 class가 키라서 안 됨 
# print(soup.find_all(class_='sister')) #그래서 _ 붙임

#get은 속성 안의 값 리턴할 때 씀

