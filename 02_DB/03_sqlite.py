import sqlite3, os

path = os.path.dirname(__file__)
conn = sqlite3.connect(path + '/example.db')
cur = conn.cursor()
# select * from stocks where symbol = 'rhat'
symbol = input('종목 이름을 입력하세요. >>> ') 
#sql = "select * from stocks where symbol = '%s'" % symbol #쿼리문 만들기 #문자 만드는 세가지 방법 참고
sql = "select * from stocks  where symbol = :1" #어떤 값을 넣을 때 '?'or :1도 가능
cur.execute(sql, (symbol,)) #셀렉트는 커밋 필요 없음 #데이터는 한 건으로 들어가야 함 (묶어서! []:리스트나 ()<-튜플 문법: 데이터가 하나면 그 뒤에 ,찍기
print(cur.fetchone()) #fetch는 가져옴 
conn.close()