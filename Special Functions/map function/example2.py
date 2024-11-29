def lstval(val):
    if val % 2 == 0:
        return 'even'
    return 'odd'

print(list(map(lstval,[11,12,13,14,15])))
