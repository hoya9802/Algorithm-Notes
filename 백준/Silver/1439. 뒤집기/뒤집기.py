S = input()
res = [0,0]
check = -1
for i in range(len(S)):
    if check == S[i]:
        continue
    check = S[i]
    res[int(check)] += 1
print(min(res))