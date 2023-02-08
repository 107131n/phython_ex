import json

def save(book):
    while True:
        name = input('책 이름을 입력하세요. >>> ')
        check = 0
        for item in book:
            if item['name'] == name:
                check = 1
        if check == 0:
            break
        print('중복인 이름이 있습니다.')

        number = input('일련 번호를 입력하세요. >>> ')
        publish = input('출판사를 입력하세요. >>> ')
        book.append({'name':name, 'number':number, 'publish':publish})
        print(book)
     
def update(book):
    name = input('수정할 책 이름 >>> ')
    idx = -1
    for i, item in enumerate(book):
        if item['name'] == name:
            idx = i

        while True:
            update = input('수정할 정보 - number, publish, exit(종료))>>>')
            if update in ('number', 'publish'):
                book[idx][update] = input(f'{update}수정 내용 >>> ')
            elif update == 'exit':
                break

        print(book[idx])
        break

    if idx == -1:
        print('등록되지 않은 데이터입니다.')

def delete(book):
    name = input('삭제할 이름 입력 >>> ')
    delok = 0
    for i, item in enumerate(book):
        if item['name'] == name :
            print(item, '삭제!')
            del book[i]
            delok = 1
            break
    if delok == 0:
            print('등록되지 않은 데이터입니다.')

def cardlist(book):
    for item in book:
        print(f'''
-----------------------------------------
책    이름 : {item['name']}
일련  번호 : {item['number']}
출  판  사 : {item['publish']} ''')
            
def search(book):
    name = input('검색할 이름 입력 >>> ')
    idx = -1
    for i, item in enumerate(book):
        if item['name'] == name:
            idx = i
            print(item)
            break
    if idx == -1:
        print('등록되지 않은 데이터입니다.')

def datasave(book):
    with open('01_basic/bookcard.data','w') as f:
        json.dump(book,f,indent=2)

def dataload(book):
    with open('01_basic/bookcard.data','r') as f:
        book = json.load(f)
    return book