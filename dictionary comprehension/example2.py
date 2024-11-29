S='abcd'
print({S[ind]:S[ind]*(ind+1) for ind in range(len(S))})