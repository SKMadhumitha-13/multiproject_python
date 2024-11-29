num = 2345
digsum = 0
while num != 0:
    rem = num%10
    digsum =digsum + rem
    num //= 10

print(digsum)