import heapq

def solution(n, roads, sources, destination):
    INF = int(1e9)
    distances = [INF] * (n+1)
    graph = [[] for _ in range(n+1)]
    
    for r in roads:
        a, b = r
        graph[a].append(b)
        graph[b].append(a)
    
    def dijkstra(v):
        q = []
        heapq.heappush(q, (0, v))
        distances[v] = 0

        while q:
            dist, now = heapq.heappop(q)
            if dist > distances[now]:
                continue
            for i in graph[now]:
                cost = dist + 1
                if cost < distances[i]:
                    distances[i] = cost
                    heapq.heappush(q, (cost, i))
        
    dijkstra(destination)
    
    res = []
    for s in sources:
        if distances[s] == INF:
            res.append(-1)
            continue
        res.append(distances[s])
        
    return res