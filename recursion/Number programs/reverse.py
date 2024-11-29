def Rev(val,pos):
    if val == 0:
        return 0
    return (val % 10)* pos +Rev(val//10,pos//10)

num =153
print(Rev(num, 10**(len(str(num))-1)))