class Parent:
    var1=8
    var2=13

class Child1(Parent):
    var1=30
    var3=25

class Child2(Child1):
    var3=45
    var4=10

obj=Child2()
print(obj.var2)