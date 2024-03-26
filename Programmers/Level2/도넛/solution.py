edges = [[2, 3], [4, 3], [1, 1], [2, 1]]

def solution(edges):
    answer = [0, 0, 0, 0]

    node_cnt = dict()
    for edge in edges:
        a = edge[0]
        b = edge[1]
        if not node_cnt.get(a):
            node_cnt[a] = [0,0]
        if not node_cnt.get(b):
            node_cnt[b] = [0,0]
        node_cnt[a][0] += 1
        node_cnt[b][1] += 1
    
    


solution(edges)
