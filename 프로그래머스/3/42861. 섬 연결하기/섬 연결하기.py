from collections import deque
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, costs):
    graph = [[] for _ in range(n)]
    parent = [x for x in range(n)]
    res = 0
    for cost in costs:
        a, b, c = cost
        graph[a].append(b)
        
    costs.sort(key=lambda x: x[-1])
    costs = deque(costs)
    
    while costs:
        a, b, c = costs.popleft()
        if find_parent(parent, a) == find_parent(parent, b):
            continue
        union_parent(parent, a, b)
        res += c
        
    return res