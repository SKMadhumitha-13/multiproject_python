class A: 
    def M1(self):
        print('Hi')
    def M2(self):
        print('M2 of A')
    
class C():
    def M1(self):
        print('M1 of C')

class B(A,C):
    def M1(self):
        print('hello')
    def M3(self):
        print('M3 of B')

obj = B()
obj.M1()