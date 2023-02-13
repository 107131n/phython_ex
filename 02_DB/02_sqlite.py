import sqlite3, os

path = os.path.dirname(__file__)
conn = sqlite3.connect(path + '/example.db')
cur = conn.cursor()
cur.execute(''' 
select * from stocks
''')
#print(cur.fetchall()) #여러 개라서
for item in cur.fetchall():
    print(item[0], item[1], item[2], item[3], item[4]) #튜플이라 인덱스로 접근 가능

conn.close()