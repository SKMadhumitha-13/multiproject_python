class A():
    pass
class B(A):
    pass
class C(A):
    pass
class D(C,B):
    pass
class E(C,B):
    pass
class F(D,E):
    pass
print(F.mro())