import sys
from collections import Counter
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [0] + list(map(int, input().split()))

for i in range(1,n+1):
    lst[i] += lst[i-1]
lst = [lst[i]%m for i in range(1,n+1)]
lc = Counter(lst)
ans = 0
for k, v in lc.items():
    ans += v * (v-1) // 2
    if k == 0:
        ans += v
print(ans)