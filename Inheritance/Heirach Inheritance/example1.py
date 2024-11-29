class Parent():
    var1 = 40
class child1(Parent):
    var2 = 30
class child2(Parent):
    var3 = 50

obj = child2()
print(obj.var1)
print(obj.var3)