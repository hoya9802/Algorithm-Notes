import sys, math
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
graph = [[] for x in range(n)]

def mid_order(s,e,depth):
    if s == e:
        graph[depth].append(data[e])
        return
    root = (s+e) // 2
    graph[depth].append(data[root])
    mid_order(s, root-1, depth+1)
    mid_order(root+1, e, depth+1)

mid_order(0,len(data)-1,0)

for i in graph:
    print(' '.join(map(str, i)))