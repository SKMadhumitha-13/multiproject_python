def binary(n, res, pow):
    if n == 0:
        return res
    rem = n % 10
    res += rem *(2**pow)
    return binary (n//10, res, pow+1)

num =10110
integer_number =binary(num,0,0)
print(integer_number)