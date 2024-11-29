class A: 
    def M1(self):
        print('Hi')
    
class B(A):
    def M1(self):
        print('Hello')

obj = B()
obj.M1()