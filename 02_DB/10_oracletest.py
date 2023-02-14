##수정
import cx_Oracle 

try:
    conn = cx_Oracle.connect('SCOTT/TIGER@localhost:1521/xe')
    cur = conn.cursor()
    cur.execute('select * from dept')
    print(cur.fetchall())
    sql = 'update dept set DNAME = :1, LOC = :2 WHERE DEPTNO = :3' #여기는 ? 안 됨
    deptno = input('부서코드 >>> ')
    dname = input('수정할 부서 이름 >>> ')
    loc = input('수정할 지역 이름 >>> ')
    data = (dname,loc,deptno)
    cur.execute(sql, data)
    conn.commit()
    conn.close()
except Exception as e:
    print(e)


