def Binary(num,pos = 1, res = 0):
    while num!= 0:
        rem =num % 2
        res += rem *pos
        pos *= 10
        num //= 2
    return res
print(list(map(Binary,range(50,101))))