import sys
sys.setrecursionlimit(10000)

def solution(maps):
    graph = [list(maps[x]) for x in range(len(maps))]
    def dfs(x, y):
        if x < 0 or x >= len(maps) or y < 0 or y >= len(maps[0]) or graph[x][y] == 'X':
            return 0
        temp = int(graph[x][y])
        graph[x][y] = 'X'
        return temp + dfs(x-1,y) + dfs(x+1, y) + dfs(x,y+1) + dfs(x,y-1)
    
    ans = []
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            res = dfs(i,j)
            if res != 0:
                ans.append(res)
    if not ans:
        return [-1]
    return sorted(ans)