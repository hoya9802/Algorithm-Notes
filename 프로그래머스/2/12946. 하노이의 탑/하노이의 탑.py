# solve 4

def solution(n):
    ans = []
    def hanoi(n, start, target, sub):
        if n == 1:
            ans.append([start, target])
            return
        hanoi(n-1, start, sub, target)
        ans.append([start, target])
        hanoi(n-1, sub, target, start)
    hanoi(n, 1, 3, 2)
    return ans