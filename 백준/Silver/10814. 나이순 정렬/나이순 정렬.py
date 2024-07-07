import sys
input = sys.stdin.readline

lst = []
for i in range(int(input())):
    name, age = input().split()
    lst.append((name, age, i))

lst.sort(key=lambda x: (int(x[0]), x[2]))
for i in lst:
    print(i[0], i[1])