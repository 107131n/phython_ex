import cx_Oracle

conn = cx_Oracle.connect('SCOTT/TIGER@localhost:1521/xe')

cur = conn.cursor()

sql = 'select * from emp'

cur.execute(sql)
for item in cur.fetchall(): #fetchall() 없어도 똑같음
    print(item)

conn.close()























# 컨트롤 쉬프트 물결 
# pip list <- 설치된 라이브러리
# conda list
# python --version
# conda --envs
# conda info --envs
# conda info --envs
# conda create -n my_project python=3.7 
# conda env list
# activate my_project 변경, 아예 벗어나려면 de
# conda list
# pip list
# python --version
# conda env list
# activate base
# conda env remove -n my_project
# conda env list
# deactivate
# activate base
# pip install cx_oracle