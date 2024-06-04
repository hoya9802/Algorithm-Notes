import sys
input = sys.stdin.readline

n = int(input())
line = 1
while n > line:
    n -= line
    line += 1
if line % 2 == 0:
    m = line - (n-1); b = n
if line % 2 != 0:
    m =n; b = line - (n-1)

print(f'{b}/{m}')