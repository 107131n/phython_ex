# 은행 계좌(Account)를 클래스로 작성하시오.
# 클래스 변수를 이용하여 계좌가 개설된 건수를 체크하고 출력하는 클래스 함수를 작성합니다.
#  클래스 함수
#  @classmethod
#  def get_account_num(cls):
#    pass

# 아래의 내용은 인스턴스 함수와 변수로 작성합니다.
# 계좌는 이름과 금액을 입력받고 계좌번호는 자동으로 생성합니다.
# 입금은 0보다 큰 금액을 입력해야하며 로그에 입금 내역을 기록합니다.
# 입금 횟수에 따라 1%의 이자가 지급됩니다.(5회마다)
# 출금은 잔액보다 작거나 같은 경우에 처리됩니다. 로그에 출금 기록을 남깁니다.
# 계좌 정보를 출력하는 함수는 예금주, 계좌 번호, 잔고를 출력합니다.
# 입금 내역과 출금 내역을 출력하는 함수.
# def deposit(): 입금 처리
# 	pass
# def withdraw(): 출금 처리
# 	pass
# def displayinfo(): 계좌 정보 출력 함수
# 	pass

class Account:
    
    account_count = 0 # 계좌가 개설된 건수
    @classmethod

    def get_account_num(cls):
        return Account.account_count

    def __init__(self, name, balance):
        Account.account_count += 1
        self.accountnumber = Account.account_count
        self.name = name
        self.balance = balance
        self.total_log = []
        self.deposit_count = 0

    def deposit(self,amount): # 입금 처리
        if  amount >= 1:
            self.total_log.append(('입금', amount))
            self.balance += amount
            self.deposit_count += 1
            print(amount, '원 입금 처리 완료!')
        if self.deposit_count % 5 == 0:
            interest = round(self.balance * 0.01,-1)
            self.balance += interest
            self.total_log.append(('이자', interest))
            print('interest', '원의 이자가 지급되었습니다.')

    def withdraw(self, amount): # 출금 처리
        if self.balance >= amount:
            self.total_log.append(('출금',amount))
            self.balance -= amount
            print(amount,'원 출금 처리 완료!')
        else:
            print('잔고가 부족합니다.')

    def displayinfo(self): # 계좌 정보 출력 함수
        print(self.__str__())

    def __str__(self):
        return f'예금주:{self.name}, 계좌번호: {self.accountnumber}, 잔고: {self.balance}'
    


# print(Account.account_count)
print(Account.get_account_num())
a = Account('홍길동', 2000)
a.displayinfo()
a.deposit(5000)
a.displayinfo()
a.withdraw(4000)
a.displayinfo()
a.withdraw(4000)
a.displayinfo()
print(a.total_log)