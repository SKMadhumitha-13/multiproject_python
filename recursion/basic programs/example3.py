def even(n):
    if n == 102:
        return
    if n % 2 == 0:
        print(n)

    even(n+1)
num=51
even(num)