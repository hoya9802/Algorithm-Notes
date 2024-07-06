import sys
input = sys.stdin.readline

lst = []
for _ in range(int(input())):
    lst.append(tuple(map(int, input().split())))

for i in sorted(lst, key=lambda x : (x[0], x[1])):
    print(i[0], i[1])