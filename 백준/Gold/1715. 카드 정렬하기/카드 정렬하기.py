import sys, heapq
input = sys.stdin.readline

q = []
for _ in range(int(input())):
    heapq.heappush(q, int(input()))

ans = 0
while len(q) > 1:
    first = heapq.heappop(q)
    second = heapq.heappop(q)
    ans += first + second
    heapq.heappush(q, first+second)
print(ans)