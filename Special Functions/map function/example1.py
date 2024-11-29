def multi(ch):
    return ch*3

obj = map (multi,'abcd')
for ele in obj:
    print(ele)