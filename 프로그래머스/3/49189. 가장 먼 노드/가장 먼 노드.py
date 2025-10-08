import heapq

def solution(n, edge):
    INF = int(1e9)
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    def dijkstra(v):
        distance[v] = 0
        q = []
        heapq.heappush(q, (0, v))
        
        while q:
            dist, now = heapq.heappop(q)
            if dist > distance[now]:
                continue
            for i in graph[now]:
                cost = dist + 1
                if cost < distance[i]:
                    distance[i] = cost
                    heapq.heappush(q, (cost, i))
        
    dijkstra(1)
    
    return sum([1 for i in distance[1:] if i == max(distance[1:])])