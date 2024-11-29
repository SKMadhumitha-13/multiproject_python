class Parent:
    def Method1(self):
        print('Method1 of Parent Class')

    def Method2(self):
        print('Method2 of Parent Class')

class Child(Parent):
    def Method1(self):
        print('Method1 of Child Class')

    def Method3(self):
        print('Method3 of Child Class')

obj=Child()
obj.Method2()