def Singleton(arg):
    L=[]
    def Inner():
        if len(L) == 0:
            L.append(arg())
        return L[0]
    return Inner

@Singleton
class Pushpa2():
    def __init__(self):
        self.totaltickets = 200

    def Booking(self):
        reqtic =int(input("Enter the number of Tickets to be booked: "))

        if reqtic <=self.totaltickets:
            print('Tickets are Booked Successfully..')

            self.totaltickets -= reqtic
            print(f'Available tickets are {self.totaltickets}')

        else:
            print("Tickets are Not-Available..")

def BookmyShow():
    print('1)Pushpa2')
    choice = int(input("Enter the movie choice :"))

    if choice == 1:
        user = Pushpa2()
        user.Booking()

    else:
        print('No Movie are available..')

def PayTM():
    print('1)Pushpa2')
    choice = int(input("Enter the movie choice :"))

    if choice == 1:
        user = Pushpa2()
        user.Booking()

    else:
        print('No Movie are available..')

def JustBook():
    print('1)Pushpa2')
    choice = int(input("Enter the movie choice :"))

    if choice == 1:
        user = Pushpa2()
        user.Booking()

    else:
        print('No Movie are available..')

def Amazon():
    print('1)Pushpa2')
    choice = int(input("Enter the movie choice :"))

    if choice == 1:
        user = Pushpa2()
        user.Booking()

    else:
        print('No Movie are available..')

print('1)BookmyShow \n2)PayTM \n3)JustBook \n4)Amazon')

user1 = int(input("Enter the booking app choice :"))

if user1 == 1:
    BookmyShow()

elif user1 == 2:
    PayTM()

elif user1 == 3:
    JustBook()

elif user1 == 4:
    Amazon()

else:
    print('Invalid choice!!')