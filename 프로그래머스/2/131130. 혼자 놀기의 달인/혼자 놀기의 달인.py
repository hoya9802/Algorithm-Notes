from collections import Counter

def solution(cards):
    
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
    parent = [x for x in range(len(cards)+1)]
    for idx, card in enumerate(cards):
        union_parent(idx+1, card)
    for i in range(1, len(parent)):
        parent[i] = find_parent(parent, i)
    cp = Counter(parent[1:])
    if len(cp) == 1:
        return 0
    res = sorted(cp.values(), reverse=True)
    return res[0] * res[1]