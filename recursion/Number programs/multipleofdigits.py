def multi(n):
    if n == 0:
        return 1
    return (n % 10) * multi(n//10)

num =1234
print(multi(num))