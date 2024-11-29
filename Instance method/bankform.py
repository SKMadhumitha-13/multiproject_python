class SBI:
    ROI=0.07
    def __init__ (self,cname,mobileno,Aadhar,PAN,Gender,Bal):
        self.cname    = cname
        self.mobileno = mobileno
        self.Aadhar = Aadhar
        self.PAN      = PAN
        self.Gender   = Gender
        self.Bal      = Bal

    def Details(self):
        print(f'Name       :{self.cname}')
        print(f'Mobile No  : {self.mobileno}')
        print(f'Aadhar No  : {self.Aadhar}')
        print(f'PAN No     : {self.PAN}')
        print(f'Gender     : {self.Gender}')
        print(f'Balance    : {self.Bal}')

    def Withdraw(self):
        amount = int(input('Enter the amount to be withdrawed:'))
        if self.Bal>=amount:
            self.Bal-=amount
            print('Amount successfully debited')
            print(f'Available balance is {self.Bal}')

        else:
            print('Insufficient Fund..')

    def Deposit(self):
        amount=int(input('Enter the amount to be credited:'))
        self.Bal+= amount
        print('Amount has been successfully credited')
        print(f'Available balance is {self.Bal}')

cust1=SBI('Madhu',8270588699,123456789012,'ASHM1234','Female',10000)
cust2=SBI('Dharik',8270585699,451234567890,'Math5694','Male',12000)

cust1.Details()
cust1.Withdraw()
cust1.Deposit()