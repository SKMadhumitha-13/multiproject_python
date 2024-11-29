class Parent:
    var1=8
    var2=10

class Child(Parent):
    var2=300
    var3=40

obj=Child()
print(obj.var1)
print(obj.var2)