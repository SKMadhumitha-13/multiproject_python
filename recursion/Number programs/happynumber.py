def happy(n):
    if n <= 9:
        return n ==1 or n == 7
    return happy(sq(n))

def sq(val):
    if val == 0:
        return 0
    return (val % 10)**2 + sq(val//10)

num = 19
print('happy Number' if happy(num) else'Not happy number')
