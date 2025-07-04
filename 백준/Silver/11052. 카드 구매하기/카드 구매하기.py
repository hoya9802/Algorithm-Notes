import sys
input = sys.stdin.readline

n = int(input())
p = [0] + list(map(int, input().split()))

for i in range(1, n+1):
    for j in range(i, n-i+1):
        tmp = p[i] + p[j]
        if p[i+j] < tmp:
            p[i+j] = tmp

print(p[-1])