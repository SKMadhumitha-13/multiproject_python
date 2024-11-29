class A():
    def Method1(self):
        print('M1 of A')

    def Method2(self):
        print('M2 of A')

class B(A):
    def Method2(self):
        print('M2 of B')
        super().Method2()

    def Method3(self):
        print('M3 of B')
        super().Method1

obj=B()
obj.Method2()