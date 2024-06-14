from collections import deque

def solution(n):
    res = deque()
    while n > 0:
        if n%3 == 0:
            res.appendleft('4')
            n -= 1
        else:
            res.appendleft(str(n%3))
        n //= 3
    return ''.join(res)