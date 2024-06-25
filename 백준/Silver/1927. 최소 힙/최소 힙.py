import sys, heapq
input = sys.stdin.readline

q = []
for _ in range(int(input())):
    cmd = int(input())
    if cmd == 0:
        if not q:
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q, cmd)