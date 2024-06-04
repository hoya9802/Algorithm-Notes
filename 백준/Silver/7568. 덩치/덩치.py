import sys
input = sys.stdin.readline

n = int(input())
lst = []; rank = [0] * n
for _ in range(n):
    lst.append(list(map(int, input().split())))

for i in range(len(lst)):
    r = 1
    for j in range(len(lst)):
        if i == j:
            continue
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            r += 1
    rank[i] = r
for r in rank:
    print(r, end=" ")