def Sign(arg):
    def conversion(n1,n2):
        if n2 == 0:
            arg(n1,1)
        else:
            arg(n1,n2)
    return conversion

@Sign
def division(val1,val2):
    print(val1/val2)

division(0,0)
division(2,0)
division(3,3)