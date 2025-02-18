#콘솔형 고객 정보 관리 시스템 구축

import re
custlist=[]
page=-1

while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    ''').uppper

    if choice=="I":
        customer={'name':'','gender':'',"email":'',"birthyear":''}        
        print("고객 정보 입력")
        customer['name'] = input('이름 >>> ')
        while True:
            customer['gender'] = input('성별(M,m or F,f) >>> '). upper()
            if customer['gender'] in ('M', 'F'):
                break
        
        while True:
            customer['email'] = input('이메일 >>> ')
            check = None
            for idx, i in enumerate(custlist):
                check = idx
                break
            if check == None:
                p = re.compile('@[a-z]{2,}[.][a-z]{2,}') 
                if p.search(customer['email']) != None:
                    break
                else:
                    print('중복인 이메일이 있습니다.')
        
        while True:
            customer['birthyear'] = input('출생년도(4자리) >>> ')
            try:
                int(customer['birthyear'])
            except:
                print('숫자를 입력하세요.')
            else:
                if len(customer['birthyear']) == 4:
                    break
                else:
                    print('4자리로 입력해주세요.')
            print(customer)
            custlist.append(customer)
            page = len(custlist)-1

    elif choice=="C":
        if page >= 0:
            print(f'현재 페이지는 {page+1}페이지입니다.')
            print(custlist[page])
        else:
            print('입력된 정보가 없습니댜.')

    elif choice=="P":
        if page <= 0:
            print('첫번째 페이지입니다.')
            print(page)
        else:
            page -= 1
            print(f'현재 페이지는 {page+1}페이지입니다.')
            print(custlist[page])


    elif choice=="N":
        if page >= len(custlist)-1:
            print('마지막 페이지입니다.')
            print(page)
        else:
            page += 1
            print(f'현재 페이지는 {page+1}페이지입니다.')
            print(custlist[page])

    elif choice=="D":
        email = input('삭제할 고객의 이메일을 입력하세요. >>> ').strip()
        delok = 0
        for idx, i in enumerate(custlist):
            if i['email'] == email:
                data = custlist.pop(idx)
                print(f'{}님의 정보가 삭제되었습니다.'.format(data['name']))
                delok = 1
                break
            if delok == 0:
                print('등록되지 읺은 이메일입니다.')
            print(custlist)
            page = len(custlist)-1
# 입력한 이메일과 일치하는 고객 정보의 인덱스를 idx에 입력
# -> idx의 default 값은 -1
# -> 일치 여부 확인 후에도 idx가 -1일 경우 등록되지 않았다고 출력
# 이메일 외에 이름, 성별, 출생년도 중 수정할 정보 선택
# 수정할 정보 선택 후 수정할 내용 입력
# 수정하고픈 변수가 없는 경우 exit 입력 시 수정창 종료
           
    elif choice=="U":
        email = input('수정할 고객의 이메일을 입력하세요. >>> ')
        idx = -1
        for idx, i in enumerate(custlist):
            print(id, i)
            if i['email'] == email:
                print(i['email'])
                idx = id
                break
        if idx == -1:
            print('등록되지 않은 이메일입니다.')
        else:
            key = input('''
다음 중 수정할 항목은(name, gender, birthyear) 
수정할 정보가 없으면 enter >>> ''')
        if key in ('name','gender','birthyear'):
            custlist[idx][key] = input('수정할 {}를 입력하세요.'.format(key))
 






    elif choice=="Q":
        print("프로그램 종료")
        break

    else:
        print('메뉴를 잘못 선택했습니다.')