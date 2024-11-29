num = 10
facount = 0
for deno in range (1,num+1):
    if num % deno == 0:
        facount += 1
if facount == 2:
    print("Prime Number")
else:
    print("Not Prime Number")