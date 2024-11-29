class Parent1():
   def money(self):
      print('10 lakh')

class Parent2():
   def money(self):
      print('20 lakh')

class Child(Parent2,Parent1):
    def money(self):
       Parent1.money(self)
       Parent2.money(self)
       print('100')

obj = Child()
obj.money()