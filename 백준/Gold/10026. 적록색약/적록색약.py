import sys, copy
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
N = int(input())

graph = []
for _ in range(N):
    graph.append(list(input().rstrip()))
graph_c = copy.deepcopy(graph)
def norm_dfs(x, y, color):
    if x < 0 or x >= len(graph) or y < 0 or y >= len(graph[0]) or graph[x][y] != color:
        return False
    graph[x][y] = 'X'
    norm_dfs(x-1,y,color); norm_dfs(x+1,y,color); norm_dfs(x,y-1,color); norm_dfs(x,y+1,color)
    return True

def pro_dfs(x, y, color):
    if color == 'B':
        if x < 0 or x >= len(graph) or y < 0 or y >= len(graph[0]) or graph[x][y] != color:
            return False
    else:
        if x < 0 or x >= len(graph) or y < 0 or y >= len(graph[0]) or graph[x][y] == 'B' or graph[x][y] == 'X':
            return False
    graph[x][y] = 'X'
    pro_dfs(x-1,y,color); pro_dfs(x+1,y,color); pro_dfs(x,y-1,color); pro_dfs(x,y+1,color)
    return True

norm_count = 0; pro_count = 0
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] != 'X' and norm_dfs(i,j,graph[i][j]):
            norm_count += 1
graph = graph_c
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if pro_dfs(i,j,graph[i][j]):
            pro_count += 1
print(norm_count, pro_count)