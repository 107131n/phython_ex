import cx_Oracle

try:
    conn = cx_Oracle.connect('SCOTT/TIGER@localhost:1521/xe')
    cur = conn.cursor()
    sql = 'insert into dept values(:1,:2,:3)' #여기는 ? 안 됨
    data = [(50,'DATABASE','SEOUL')]
    cur.executemany(sql, data)
    conn.commit()
    conn.close()
except Exception as e:
    print(e)
    print('중복되는 값입니다.')

print('계속 진행!!')
