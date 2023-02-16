''' 명함 관리 프로그램

데이터는 오라클에 저장 tablename : namecard
				- cardid (숫자값, 기본키, 자동 증가)
				- name
				- address
				- tel
				- email
프로그램 메뉴 - 명함 추가, 명함 수정, 명함 삭제, 명함 검색, 명함 리스트, 종료

필요한 기능은 함수로 작성하세요
- table 생성 : create_table() 
- 명함 추가 : add_card() 
- 명함 수정 : update_card()  
- 명함 삭제 : delete_card()
- 명함 검색 : search_card() 
- 명함 리스트 : list_card() '''

import namecard as nc, sys
nc.create_table()

while True:
	display = '''
----------------------------------------------------------------------
1.명함 추가 2.명함 수정 3.명함 삭제 4.명함 검색 5.명함 리스트 6.종료    
>>> '''
	menu = input(display)
	if menu == '1':
		nc.insert_card()
	elif menu == '2':
		nc.update_card()
	elif menu == '3':
		nc.delete_card()
	elif menu == '4':
		nc.search_card()
	elif menu == '5':
		nc.list_card()
	elif menu == '6': # break는 while문 벗어나게 # sys._exit()는 그 지점에서 프로그램 종료 # return은 함수 종료
		print('프로그램 종료!')
		sys._exit() 
	else:
		print('메뉴 선택을 잘못하셨습니다.')