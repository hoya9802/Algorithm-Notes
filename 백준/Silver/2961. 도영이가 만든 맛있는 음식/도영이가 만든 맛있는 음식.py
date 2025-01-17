import sys
input = sys.stdin.readline

n = int(input())
ingredients = [list(map(int, input().split())) for _ in range(n)]

res = int(1e9)
def dfs(idx, s, b, count):
    global res

    if idx == n:
        if count > 0:
            res = min(res, abs(s-b))
        return

    dfs(idx+1, s*ingredients[idx][0], b+ingredients[idx][1], count+1)

    dfs(idx+1, s, b, count)

dfs(0, 1, 0, 0)
print(res)