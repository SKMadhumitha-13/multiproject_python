def Outer(arg):
    L=[]
    def Inner():
        if len (L) == 0:
            obj = arg()
            L.append(obj)
        return L[0]          # To call the particular obj, we are returning to call this method.
    return Inner

@Outer
class M15():
    def __init__(self):
        print('executed')

M15()
M15()
M15()