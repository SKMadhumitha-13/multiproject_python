def factorial (num):
    if num == 0 or num == 1:
        return 1
    return num*factorial (num-1)
def Strong (val):
    if val == 0:
        return 0
    return factorial (val%10) + Strong(val//10)

num= 145
print('Strong Number' if Strong(num)== num else 'Not Strong Number')