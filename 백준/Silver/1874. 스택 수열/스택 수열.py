import sys
input = sys.stdin.readline

n = int(input())

arr = [int(input()) for _ in range(n)]
res = []

target = 0; stack = []
for i in range(n):
    stack.append(i+1)
    res.append('+')
    while target < len(arr) and stack and arr[target] == stack[-1]:
        stack.pop()
        res.append('-')
        target += 1

print('\n'.join(res) if not stack else 'NO')
