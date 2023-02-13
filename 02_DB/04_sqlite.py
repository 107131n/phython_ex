import sqlite3, os

path = os.path.dirname(__file__)
conn = sqlite3.connect(path + '/example.db')
cur = conn.cursor()
sql = 'insert into stocks values(?,?,?,?,?)' #추가
# data = ('2022-1-8','buy','ibm',1000,45.00) 
# cur.execute(sql, data) 
data = [('2022-1-8','buy','ibm',1000,45.00),
        ('2022-7-8','sell','ibm',500,4.00),
        ('2022-1-18','buy','msft',400,72.00),
        ('2022-12-9','buy','rhat',120,37.00),
        ('2022-9-8','buy','ibm',700,50.00)]
cur.executemany(sql, data) 
conn.commit() 
conn.close() 


