class Class1():
    pass
class Child1(Class1):
    pass
class Child2 (Class1):
    pass
class Gchild(Child1,Child2):
    pass

obj= Gchild()
