import namecard as nc, os
import pickle


# 클래스 Card,   CardBook
# -------------------------------------------------------------------------------
# 1. CardBook 생성 2. Card추가 3. Card삭제 4. Card내용 보기 5. 전체목록 보기 6. 종료

# 전체목록 보기 정렬하는 키를 입력받아서 정렬해 출력
# 데이터는 피클로 저장

path = os.path.dirname(__file__)
# print(__file__)
# print(path)
cardbook = None

# with open(path+'/cardbook1.pickle', 'rb') as f:
#       cardbook = pickle.load(f)

while True: 
    menu = input('''
----------------------------------------------------------------------------------
1. CardBook생성 2. Card추가 3. Card삭제 4. Card내용 보기 5. 전체목록 보기 6. 종료
>>> ''')
    if menu == '1':
          if cardbook == None:
               cardbook = nc.CardBook(input('타이틀을 입력하세요 >>> '))
          else:
               print('생성된 카드북이 존재합니다') 

    elif menu == '2':
          try:     
               name = input('name >>> ')
               address = input('address >>> ')
               tel = int(input('tel >>> '))
               email = input('email >>> ')
               card = nc.Card(name, address, tel, email)
               cardbook.add_card(card)           
          except IndexError:
               print('인덱스 오류')               
          except Exception as e:
               print(e)
               print('카드북 생성한 후 가능합니다')

    elif menu == '3':
          if cardbook == None:
               print('카드북 생성한 후 가능합니다')
          else:
               print(list(cardbook.cards.keys()))
               page = int(input('page_number >>> '))
               card = cardbook.remove_card(page)
               print(card, '-> 삭제')

    elif menu == '4':
          if cardbook == None:
               print('카드북 생성한 후 가능합니다')
          else:
               print(list(cardbook.cards.keys()))
               page = int(input('page_number >>> '))
               card = cardbook.cards[page]
               print(card)
               
    elif menu == '5':
          if cardbook == None:
               print('카드북 생성한 후 가능합니다.')
          else:
               key = input('정렬 키(입력값:name, address, tel, email) >>> ')
               sort = bool(input('오름차순(enter), 내림차순(1) >>> '))
               #print(sort,type(sort))
               if key in ('name', 'address', 'tel', 'email'):
                    cardbook.list_cards(key, sort)
               else:
                    cardbook.list_cards(reverse=sort)

    elif menu == '6':
         print('프로그램 종료')
         break

with open('01_basic/cardbook1.pickle', 'wb') as f:
     pickle.dump(cardbook, f) 
