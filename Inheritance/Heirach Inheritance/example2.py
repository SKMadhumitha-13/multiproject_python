class Money():
    def __init__(self,bal):
        self.bal = bal
    def Withdraw (self):
        amount = int(input('Enter the amount to be withdrawed:'))
        self.bal -= amount
        print(f'Availalble Bal is {self.bal}')

    def Deposite (self):
        amount = int(input('Enter Amount to be deposited: '))
        self.bal += amount
        print(f'Available Bal is {self.bal}')

class Swiss(Money):
    def __init__ (self,bal):
        super().__init__(bal)

class SBI(Money):
    def __init__(self,bal):
        super().__init__(bal)

user1 = SBI(5000)
user1.Withdraw()
user1.Deposite()