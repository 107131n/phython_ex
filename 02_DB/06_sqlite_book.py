import book

book.create_table()

while True:
    prompt = '''
------------------------------------------------------------------------------
1.책 정보 등록 2.책 정보 수정 3.책 정보 삭제 4.책 리스트 출력 5.검색 6.종료      
>>> '''
    menu = input(prompt)
    if menu == '1':
        try:
            book.insert_books()
        except Exception as e:
            print(e)

    elif menu == '2':
        title = input('수정할 책 제목 >>> ')
        idx = -1
        for i, item in enumerate(book):
            if item['title'] == title:
                idx = i

            while True:
                update = input('수정할 정보 - published_date, publisher, pages, recommend, exit(종료))>>>')
                if update in ('published_date', 'publisher', 'pages', 'recommend'):
                    book[idx][update] = input(f'{update}수정 내용 >>> ')
                elif update == 'exit':
                    break
            print(book[idx])
            break
        if idx == -1:
            print('등록되지 않은 데이터입니다.')    

    elif menu == '3':
        title = input('삭제할 책 제목 입력 >>> ')
        delok = 0
        for i, item in enumerate(book):
            if item['title'] == title:
                print(item, '삭제!!')
                del book[i]
                delok = 1
                break
        if delok == 0:
            print('등록되지 않은 데이터입니다.') 

    elif menu == '4':
        for item in book:
            print(f'''
--------------------------------------------------
책 제목: {item['title']}
출판일: {item['published_date']}
출판사: {item['publisher']}
장 수: {item['pages']}
추천 여부: {item['recommend']} ''')
            
    elif menu == '5':
        title = input('검색할 책 제목 입력 >>> ')
        idx = -1
        for i, item in enumerate(book):
            if item['title'] == title:
                idx = i
                print(item)
                break
        if idx == -1:
            print('등록되지 않은 데이터입니다.')

    elif menu == '6':
        print('프로그램 종료!')
        break

    else:
        print('메뉴 선택을 잘못하셨습니다.')