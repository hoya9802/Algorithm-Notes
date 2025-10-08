from collections import deque

def solution(n, costs):
    parent = [i for i in range(n)]
    costs.sort(key=lambda x: x[-1])
    q = deque(costs)
    
    def find(parent, a):
        if parent[a] != a:
            parent[a] = find(parent, parent[a])
        return parent[a]

    def union(a, b):
        a = find(parent, a)
        b = find(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    
    ans = 0
    while q:
        a, b, c = q.popleft()
        if find(parent, a) != find(parent, b):
            union(a, b)
            ans += c
        else:
            continue
    
    return ans
            
        