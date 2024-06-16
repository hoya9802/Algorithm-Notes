def solution(n):
    res = []
    def hanoi(n, start, target, sub):
        if n == 1:
            res.append([start, target])
            return
        hanoi(n-1, start, sub, target)
        res.append([start, target])
        hanoi(n-1, sub, target, start)
    hanoi(n, 1, 3, 2)
    return res