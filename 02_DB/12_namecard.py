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

import namecard #동작 안 됨
while True:
	prompt = '''
-------------------------------------------------------------------------
1.명함 추가 2.명함 수정 3.명함 삭제 4.명함 검색 5.명함 리스트 6.종료    
>>> '''
	menu = input(prompt)
	if menu == '1':
		try:
			namecard.insert_card()
		except Exception as e:
			print(e)
		
	elif menu == '2':
		cardid = input('수정할 등록번호 >>> ')
		idx = -1
		for i, item in enumerate(namecard):
			if item['cardid'] == cardid:
				idx = i
			while True:
				update = input('수정할 정보 - name, tel, address, email')
				if update in ('name', 'tel', 'address', 'email'):
					namecard[idx][update] = input(f'{update}수정 내용 >>>')
				elif update == 'exit':
					break
			print(namecard[idx])
			break
		if idx == -1:
			print('등록되지 않은 데이터입니다.')
		
	elif menu == '3':
		cardid = input('삭제할 등록번호 입력 >>>')
		delok = 0
		for i,0i0tem in enumerate(namecard):
			print(item, '삭제!!')
			del namecard[i]
			delok = 1
			break
		if delok == 0:
			print('등록되지 않은 데이터입니다.')
		
	elif menu == '4':
		for item in namecard:
			print(f'''
----------------------------------------------------------------------
cardid : {item['cardid']}
name : {item['name']}
tel : {item['tel']}
address : {item['address']}
email :	{item['email']} ''')
		
	elif menu == '5':
		cardid = input('검색할 등록번호 입력 >>> ')
		idx = -1
		for i, item in enumerate(namecard):
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