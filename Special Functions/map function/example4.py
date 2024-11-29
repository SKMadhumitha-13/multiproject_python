def Prime (num):
    for deno in range(2, num//2+1):
        if num % deno == 0:
            return 'NP'
        
    return 'Prime'

print(list(map(Prime,[14,15,16,17,20,21])))