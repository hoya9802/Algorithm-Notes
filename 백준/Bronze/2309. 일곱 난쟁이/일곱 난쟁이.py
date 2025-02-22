import sys
input = sys.stdin.readline

heights = [int(input()) for _ in range(9)]
res = []
def dfs(lst, total, n, i):
    global res
    if len(lst) == 7:
        if total == 100:
            res = sorted(lst)
        return
    if i > 8:
        return

    dfs(lst+[heights[i]], total+heights[i], n+1, i+1)
    dfs(lst, total, n, i+1)

dfs([], 0, 0, 0)

print('\n'.join(map(str, res)))