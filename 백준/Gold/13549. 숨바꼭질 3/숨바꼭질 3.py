import sys, heapq
input = sys.stdin.readline

n, k = map(int, input().split())
INF = int(1e9)
timerecord = [INF] * (100001)
timerecord[n] = 0
q = []
heapq.heappush(q, (0, n))

while q:
    time, now = heapq.heappop(q)
    if now == k:
        break
    if timerecord[now] < time:
        continue
    for cmd in range(3):
        if cmd == 0:
            cost = time + 1
            if 0 <= now+1 < len(timerecord) and cost < timerecord[now+1]:
                timerecord[now+1] = cost
                heapq.heappush(q, (cost, now+1))
        if cmd == 1:
            cost = time + 1
            if 0 <= now-1 < len(timerecord) and cost < timerecord[now-1]:
                timerecord[now-1] = cost
                heapq.heappush(q, (cost, now-1))
        if cmd == 2:
            cost = time
            if now*2 < len(timerecord) and cost < timerecord[now*2]:
                timerecord[now*2] = cost
                heapq.heappush(q, (cost, now*2))

print(timerecord[k])