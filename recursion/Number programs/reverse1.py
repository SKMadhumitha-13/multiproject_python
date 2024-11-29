def reverse(n,pos):
    if n == 0:
        return pos
    pos = (pos*10) + (n % 10)
    return reverse(n // 10, pos)

num =1234
reverse_number = reverse(num,0)
print(reverse_number)