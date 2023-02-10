# 계좌 개설 - 계좌를 새로 만듭니다.
# 입금 - 계좌번호를 입력 받아 여러 계좌 중에서 계좌번호 일치하는 계좌에 입금
# 출금 - 계좌번호를 입력 받아 계좌번호 일치하는 계좌에 출금 처리
# 계좌 로그 - 계좌 번호를 입력 받아서 해당 계좌의 로그를 출력
# 계좌 정보 - 계좌 번호를 입력 받아서 계좌 정보를 조회
# 계좌 리스트 - 전체 계좌를 목록으로 출력(정렬 기능 유)
# 종료 - 종료 시 데이터는 파일로 저장
# 시작 - 프로그램 시작 시 데이터 파일을 로드

from Account import Account # Account.deposit()
import Account              # Account.Account.deposit()
account_list = []

while True:
    display = '''
--------------------------------------------------------------
1. 계좌 개설 2. 입금 3. 출금 4. 계좌 로그 5. 계좌 정보 6. 종료
--------------------------------------------------------------
>>>  '''
    menu = input(display)
    if menu == '1':
        if account_list == None:
            account_list = Account(input('계좌를 입력하세요 >>> '))
        else:
            print('생성된 계좌가 존재합니다.')

    elif menu == '2':
        pass
    elif menu == '3':
        pass
    elif menu == '4':
        pass
    elif menu == '5':
        pass
    elif menu == '6':
        pass
    elif menu == '7':
        pass
    else:
        print('메뉴를 잘못 선택하셨습니다.')



