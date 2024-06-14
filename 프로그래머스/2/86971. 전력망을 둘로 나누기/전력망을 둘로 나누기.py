def solution(n, wires):
    
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
    ans = int(1e9)
    for i in range(len(wires)):
        parent = [x for x in range(n+1)]
        for j in range(len(wires)):
            if i == j:
                continue
            a, b = wires[j]
            union_parent(a, b)

        for k in range(1,n+1):
            parent[k] = find_parent(parent, k)
        ans = min(ans, abs(parent.count(parent[wires[i][0]]) - parent.count(parent[wires[i][1]])))
    return ans