# 도서관리 프로그램
# 데이터 구조는 리스트를 이용
# 일련 번호, 책 이름, 출판사, ...
# 1. 저장 2. 수정 3. 삭제 4. 리스트 5. 검색 6. 종료(Q)

book =[]

while True:
    menu = input('''
---------------------------------------------------
1. 저장 2. 수정 3. 삭제 4. 리스트 5. 검색 6. 종료(Q)
---------------------------------------------------
>>> ''')
    if menu == '1':
        while True:
            name = input('책 이름을 입력하세요. >>> ')
            check = 0
            for item in book:
                if item[0] == name:
                    check = 1
            if check == 0:
                break
            print('중복인 이름이 있습니다.')

        number = input('일련 번호를 입력하세요. >>> ')
        publish = input('출판사를 입력하세요. >>> ')
        book.append([name, number, publish])
        print(book)
        
    elif menu == '2':
        name = input('수정할 책 이름 >>> ')
        idx = -1
        for i, item in enumerate(book):
            if item[0] == name:
                idx = i
                update = int(input('수정할 정보(1.name, 2. number, 3.publish)>>>'))
                book[idx][update] = input('수정 내용 >>> ')
                break
                print(book[idx])
            if idx == 1:
                print('등록되지 않은 데이터입니다.')
    elif menu == '3':
        name = input('삭제할 이름 입력 >>> ')
        delok = 0
        for i, item in enumerate(book):
            if item[0] == name:
                print('삭제!')
                del book[i]
                delok = 1
                break
            if delok == 0:
                print('등록되지 않은 데이터입니다.')
    elif menu == '4':
        for item in book:
            print(f'''
-----------------------------------------
책    이름 : {item[0]}
일련  번호 : {item[1]}
출  판  사 : {item[2]}''')
    elif menu == '5':
        name = input('검색할 이름 입력 >>> ')
        idx = -1
        for i, item in enumerate(book):
            if item[0] == name:
                idx = i
                print(item)
                break
        if idx == -1:
            print('등록되지 않은 데이터입니다.')
    elif menu in ('6', 'q', 'Q'):
        print('프로그램 종료')
        break
    else:
        print('메뉴를 잘못 선택하였습니다.')
