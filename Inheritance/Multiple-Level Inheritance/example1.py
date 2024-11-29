class Parent1():
    val1 = 40
    val2 = 20

class Parent2():
    val3 = 30
    val2 = 60

class Child(Parent2,Parent1):
    val3 = 10
    val1 = 20

obj = Child()
print(obj.val3)
print(obj.val4)
