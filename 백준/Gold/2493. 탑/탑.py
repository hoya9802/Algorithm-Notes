import sys
input = sys.stdin.readline

n = int(input())
lst = [0] + list(map(int, input().split()))
res = [0] * (n+1)
stack = []

for i in range(1,n+1):
    while stack:
        if lst[i] > stack[-1][0]:
            stack.pop()
        else:
            res[i] = stack[-1][1]
            break
    
    stack.append((lst[i], i))

print(' '.join(map(str, res[1:])))