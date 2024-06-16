import sys
from collections import Counter
input = sys.stdin.readline

v, e = map(int, input().split())
parent = [x for x in range(v+1)]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(e):
    a, b = map(int, input().split())
    union_parent(a, b)

for i in range(1, v+1):
    parent[i] = find_parent(parent, i)

print(len(Counter(parent[1:])))