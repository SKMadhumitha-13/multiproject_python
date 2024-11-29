class Operation():
    def Add (self,*args):
        res = 0
        for el in args:
            res += el
        print(res)

obj = Operation()
obj.Add (4,5,1,2)
obj.Add(1,2,3)
obj.Add()