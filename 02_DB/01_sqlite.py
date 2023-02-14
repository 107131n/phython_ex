import sqlite3 #라이브러리 이름과 같으면 안 됨
import os
print(sqlite3.version) # 위에 1번 줄 버전 나타냄
print(sqlite3.sqlite_version) # 인터넷에 버전 나타냄
path =os.path.dirname(__file__)
conn = sqlite3.connect(path + '/example.db') # 디비랑 연결 # ()안에 루트랑 파일이름 # 테이블 없으면 새로 만듦
cur = conn.cursor() # 커서 개체 받아야 함 # 결과값 커서가 가짐
cur.execute(''' 
create table if not exists stocks
(date text, trans text, symbol text, qyt real, price real)
''') # 쿼리문 실행 # 대부분 익스큐트 사용
cur.execute('''
insert into stocks values('2023-01-07', 'buy', 'rhat', 100, 35.23)
''') 
conn.commit() # 변화 있는 건 커밋해야 함
conn.close() # 연결 끊어주기 다른 곳에서 사용 가능하게










#기본적으로 제공하는 라이브러리 사용
#파일로 저장, 계정과 상관없음
#sqlite browser