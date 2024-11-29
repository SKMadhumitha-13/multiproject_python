class SBI:
    ROI=0.07
    def __init__ (self,cname,mobileno,Aadhar,PAN,Gender,Bal,Pin):
        self.cname    = cname
        self.mobileno = mobileno
        self.Aadhar = Aadhar
        self.PAN      = PAN
        self.Gender   = Gender
        self.Bal      = Bal
        self.Pin      = Pin

    def Details(self):
        print(f'Name       :{self.cname}')
        print(f'Mobile No  : {self.mobileno}')
        print(f'Aadhar No  : {self.Aadhar}')
        print(f'PAN No     : {self.PAN}')
        print(f'Gender     : {self.Gender}')
        print(f'Balance    : {self.Bal}')

    def Withdraw(self):
        if self.checkpin() == self.Pin:
            amount = int(input('Enter the amount to be withdrawed:'))
            if self.Bal>=amount:
                self.Bal-=amount
                print('Amount successfully debited')
                print(f'Available balance is {self.Bal}')

            else:
                print('Insufficient Fund..')
        else:
            print("Entered Invalid PIN")

    @staticmethod
    def checkpin():
        return int(input('Enter the 4-digit PIN:'))        

    def Deposit(self):
        amount=int(input('Enter the amount to be credited:'))
        self.Bal+= amount
        print('Amount has been successfully credited')
        print(f'Available balance is {self.Bal}')

    def CheckBal(self):
        if self.checkpin() == self.Pin:
            print(f'Available Balance is {self.Bal}')

        else:
            print("Invalid Pin")

    def ChangePIN(self):
        oldpin=input()
        if self.Pin == oldpin:
            newpin = input()
            self.Pin = newpin
        else:
            print('Entered old pin is incorrect')
 
cust1=SBI('Madhu',8270588699,123456789012,'ASHM1234','Female',10000,1234)
cust2=SBI('Kanimozli',8270585699,451234567890,'Math5694','Female',12000,5678)
cust1.CheckBal()
cust1.ChangePIN()