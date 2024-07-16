import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
del_node = int(input())

def dfs(node, data):
    data[node] = -2
    for i in range(len(data)):
        if data[i] == node:
            dfs(i, data)

dfs(del_node, data)
res = 0
for i in range(len(data)):
    if data[i] != -2 and i not in data:
        res += 1
print(res)