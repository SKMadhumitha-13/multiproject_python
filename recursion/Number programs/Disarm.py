def disarm(n,pow):
    if n == 0:
        return 0
    return (n%10)**pow + disarm (n//10,pow-1)
num= 153
pow = len(str(num))
print('Disarm NUmber' if disarm (num,pow)== num else 'Not Disarm')