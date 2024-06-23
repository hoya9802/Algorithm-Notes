import sys
n, m = map(int, input().split())
fsum = [0] + list(map(int, input().split()))
for i in range(1,n+1):
    fsum[i] += fsum[i-1]

pointer = 0; res = 100000
for i in range(1,n+1):
    if fsum[i] < m:
        continue
    while pointer < i:
        if fsum[i] - fsum[pointer] >= m:
            if i - pointer < res:
                res = i - pointer
            pointer += 1
        else:
            break
if res == 100000:
    print(0)
else: print(res)