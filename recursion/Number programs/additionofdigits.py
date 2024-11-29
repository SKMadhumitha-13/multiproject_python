def add(n):
    if n == 0:
        return 0
    return n%10 + add(n//10)

num = 5678
print(add(num))