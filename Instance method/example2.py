class Phone:
    '''class variable'''
    p_name='Iphone'
    model='15pro'
    def __init__(self,ram,rom,color,camera,battery,price):
        self.ram=ram
        self.rom=rom
        self.color=color
        self.camera=camera
        self.battery=battery
        self.price=price
        print(self.color,self.price)
        

p1=Phone('4GB','128GB','SeaBlue','50px','500mAH','1.5lk')

print(p1.ram,p1.color)
print(Phone.model)
print(p1.model)