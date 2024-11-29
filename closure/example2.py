def A(arg):
    def Z(oc,nov):
        if nov == 0:
            arg(oc,1)
        else:
            arg(oc,nov)
    return Z

@A
def division(val1,val2):
    print(val1/val2)

division(0,0)
division(2,0)
division(3,2)
division(0,2)