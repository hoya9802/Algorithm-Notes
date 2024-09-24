import sys
input = sys.stdin.readline
x = input().rstrip()
y = input().rstrip()

table = [[0] * (len(x)+1) for _ in range(len(y)+1)]
for i in range(1,len(y)+1):
    for j in range(1,len(x)+1):
        if x[j-1] == y[i-1]:
            table[i][j] = table[i-1][j-1]+1
        else:
            table[i][j] = max(table[i-1][j], table[i][j-1])

print(table[-1][-1])