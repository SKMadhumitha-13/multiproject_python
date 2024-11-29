class car:
    '''class variable'''
    name='BMW'
    def __init__(self,color,model,power,engine,price):
        self.color=color
        self.model=model
        self.power=power
        self.engine=engine
        self.price=price

    def car_details(self):
        print(f'''
        car_name : {self.name}
        color    : {self.color}
        model    : {self.model}
        power    : {self.power}
        engine   : {self.engine}
        price    : {self.price}
        ''')

c1=car('White','M5',536,'V6','1cr')
c1.car_details()
