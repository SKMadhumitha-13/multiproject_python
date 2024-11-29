def Sign(arg):
    def conversion (n1,n2):
        if n1<0 and n2>0:
           return arg(n1*(-1),n2)
        elif n1>0 and n2<0:
          return arg(n1,n2*(-1))
        else:
            return arg(n1,n2)
    return conversion

@Sign
def Multiply(val1, val2):
    print(val1*val2)

Multiply(0,0)
Multiply(-2,3)
Multiply(3,-5)
Multiply(-3,-6)