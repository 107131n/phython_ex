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