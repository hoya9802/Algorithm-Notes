import sys
input = sys.stdin.readline

n = int(input())
graph = [[0]*100 for _ in range(100)]

def square(m, x, y):
    for i in range(10):
        for j in range(10):
            m[x-1+i][y-1+j] = 1

for _ in range(n):
    x, y = map(int, input().split())
    square(graph, x, y)
res = 0
for i in range(len(graph)):
    for j in range(len(graph)):
        if graph[i][j] == 1:
            res += 1
print(res)