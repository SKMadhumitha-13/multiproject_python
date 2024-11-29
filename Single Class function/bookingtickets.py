def Singleton(arg):
    L=[]
    def Inner():
        if len(L) == 0:
            #obj = arg()
            #L.append(obj)
            L.append(arg())     
        return L[0]      #To call a particular function we need to return L[0].
    return Inner
@Singleton    
class Amaran():
    def __init__(self):
        self.totaltickets = 200

    def Booking(self):
        reqtic = int (input("Enter the number of tickets: "))

        if reqtic <= self.totaltickets:
            print('Tickets Booked Successfully...')

            self.totaltickets -= reqtic
            print(f'Available tickets are {self.totaltickets}')

        else:
            print("Tickets are Not-Available ")

@Singleton    
class LubberBandhu():
    def __init__(self):
        self.totaltickets = 180

    def Booking(self):
        reqtic = int (input("Enter the number of tickets: "))

        if reqtic <= self.totaltickets:
            print('Tickets Booked Successfully...')

            self.totaltickets -= reqtic
            print(f'Available tickets are {self.totaltickets}')

        else:
            print("Tickets are Not-Available ")

@Singleton    
class SIR():
    def __init__(self):
        self.totaltickets = 180

    def Booking(self):
        reqtic = int (input("Enter the number of tickets: "))

        if reqtic <= self.totaltickets:
            print('Tickets Booked Successfully...')

            self.totaltickets -= reqtic
            print(f'Available tickets are {self.totaltickets}')

        else:
            print("Tickets are Not-Available ")

def BookMyShow():
    print('1) Amaran \n2) Lubber Bandhu \n3)SIR')
    choice = int(input("Enter the movie choice"))

    if choice == 1:
        user = Amaran()
        user.Booking()

    elif choice == 2:
        user = LubberBandhu()
        user.Booking()

    elif choice == 3:
        user = SIR()
        user.Booking()
        
    else:
        print('No Movies are available')


user1 = BookMyShow()
print('-'*20)
user2 = BookMyShow()
print('-'*20)
user3 = BookMyShow()
print('-'*20)