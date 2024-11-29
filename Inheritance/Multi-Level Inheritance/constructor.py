class V1():
    def __init__(self,name,MobNo):
       self.name = name
       self.MobNo = MobNo

    def details(self):
        print(f'{self.name}')
        print(f'{self.MobNo}')

class V2(V1):
    def __init__ (self,name,MobNo,gender,mailId):
        V1.__init__(self,name,MobNo)
        self.gender = gender 
        self.mailId =mailId

    def details(self):
        V1.details(self)
        print(f'{self.gender}')
        print(f'{self.mailId}')

user1 = V2('Hari',9876543210,'Male','hari420@gmail.com')
user1.details()
