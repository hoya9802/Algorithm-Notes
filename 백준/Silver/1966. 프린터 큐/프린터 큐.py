import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    ranks = list(map(int, input().split()))
    array = deque([(x, i) for i, x in enumerate(ranks)])

    ranks.sort()

    res = 0
    while array:
        pn, pi =  array[0]
        if ranks[-1] == pn:
            _, idx = array.popleft()
            ranks.pop()
            res += 1
            if idx == m:
                print(res)
                break
        else:
            array.append(array.popleft())
