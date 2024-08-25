import sys
input = sys.stdin.readline

lst = [0] * 30
for _ in range(28):
    lst[int(input())-1] = 1
print(*list(x+1 for x in range(len(lst)) if lst[x] != 1),sep='\n')