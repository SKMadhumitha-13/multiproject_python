def armstrong(n):
    if n == 0:
        return 0
    return (n %10)**pow + armstrong(n//10)
num = 153
pow = len(str(num))
print('Armstrong Number' if armstrong (num) == num else 'Not Armstrong')