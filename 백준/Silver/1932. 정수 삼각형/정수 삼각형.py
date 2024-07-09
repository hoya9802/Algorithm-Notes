import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp  = [[0]*x for x in range(1,n+1)]
dp[0][0] = graph[0][0]

for i in range(0, n-1):
    for j in range(len(graph[i])):
        for k in [(1,0), (1,1)]:
            temp = dp[i][j] + graph[i+k[0]][j+k[1]]
            dp[i+k[0]][j+k[1]] = max(dp[i+k[0]][j+k[1]], temp)

print(max(dp[-1]))