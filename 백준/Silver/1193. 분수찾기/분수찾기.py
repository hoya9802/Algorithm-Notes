import sys
input = sys.stdin.readline

x = int(input())
line = 1
while x > line:
    x -= line
    line += 1
if line % 2 == 0:
    t = x; b = line -(x-1)
else:
    t = line-(x-1)
    b = x
print(f'{t}/{b}')