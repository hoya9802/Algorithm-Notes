import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

def cal(x, y):
    x_val, y_val = 0, 0
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            x_val += (graph[x[i]][x[j]] + graph[x[j]][x[i]])
    for i in range(len(y)):
        for j in range(i+1,len(y)):
            y_val += (graph[y[i]][y[j]] + graph[y[j]][y[i]])
    return abs(x_val - y_val)

ans = int(1e9)
def dfs(n, a_list, b_list):
    global ans
    if len(a_list) > N//2 or len(b_list) > N//2:
        return
    if n == N:
        if len(a_list) == len(b_list):
            ans = min(ans, cal(a_list, b_list))
        return
    
    dfs(n+1, a_list+[n], b_list)
    dfs(n+1, a_list, b_list+[n])

dfs(0, [], [])
print(ans)