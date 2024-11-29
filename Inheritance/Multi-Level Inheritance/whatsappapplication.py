class V1():
    def __init__(self,name,mailId):
        self.name = name
        self.mailId = mailId

    def details(self):
        print(f'{self.name}')
        print(f'{self.mailId}')

class V2(V1):
    def __init__(self,name,mailId,AadharNo,MobNo):
        super().__init__(name,mailId)
        self.AadharNo = AadharNo
        self.MobNo = MobNo

    def details(self):
        super().details()
        print(f'{self.AadharNo}')
        print(f'{self.MobNo}')

class V3(V2):
    def __init__(self,name,mailId,AadharNo, MobNo,PAN,PIN):
        super().__init__ (name,mailId,AadharNo,MobNo)
        self.PAN = PAN
        self.PIN = PIN

    def details(self):
        super().details()
        print(f'{self.PAN}')
        print(f'{self.PIN}')

user1 = V3('Hari','hari420@gmail.com', 234578965412,9876543210,'ABNT3450',1234)
user1.details()