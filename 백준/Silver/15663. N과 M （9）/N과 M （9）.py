import sys
from collections import Counter
input = sys.stdin.readline

n, m = map(int, input().split())
data = sorted(list(map(int, input().split())))
dc = Counter(data)

res = set()
def dfs(s):
    if len(s) == m:
        res.add(tuple(s))
        return
    for i in range(len(data)):
        if dc[data[i]] > 0:
            dc[data[i]] -= 1
            s.append(data[i])
            dfs(s)
            s.pop()
            dc[data[i]] += 1

dfs([])

for i in sorted(res):
    print(' '.join(map(str, i)))