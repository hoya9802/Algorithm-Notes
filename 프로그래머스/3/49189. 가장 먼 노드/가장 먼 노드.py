import heapq

def solution(n, edge):
    INF = int(1e9)
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    distances = [INF] * (n+1)
    
    for e in edge:
        a, b = e
        graph[a].append(b)
        graph[b].append(a)

    def dijkstra(v):
        nonlocal visited, distances
        q = []
        heapq.heappush(q, (0, v))
        
        while q:
            dist, now = heapq.heappop(q)
            distances[now] = dist
            visited[now] = 1
            
            for i in graph[now]:
                if dist + 1 < distances[i]:
                    distances[i] = dist + 1
                    
                    heapq.heappush(q, (distances[i],i))
        
    dijkstra(1)
    
    max_val = 0
    for d in range(1, len(distances)):
        if distances[d] == INF:
            continue
        if distances[d] > max_val:
            max_val = distances[d]
    
    return sum([1 for i in range(1, len(distances)) if distances[i] == max_val])