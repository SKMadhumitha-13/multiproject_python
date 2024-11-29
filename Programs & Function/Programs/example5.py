num = 5078
dig = len(str(num))
pos = 10**(dig-1)
rev = 0
while num != 0:
    rem = num % 10
    rev = rev + rem*pos
    num //= 10
    pos //= 10

print(rev)