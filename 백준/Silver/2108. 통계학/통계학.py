import sys
from collections import Counter
input = sys.stdin.readline
lst = []
for _ in range(int(input())):
    lst.append(int(input()))
print(round(sum(lst)/len(lst)))
print(sorted(lst)[len(lst)//2])
cl = Counter(lst)
mx = max(cl.values())
temp = []
for x,c in cl.items():
    if c == mx:
        temp.append(x)
temp.sort()
if len(temp) == 1:
    print(temp[0])
else:
    print(temp[1])
print(max(lst)-min(lst))