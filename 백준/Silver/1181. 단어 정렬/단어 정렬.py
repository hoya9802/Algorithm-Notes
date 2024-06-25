import sys
input = sys.stdin.readline

lst = set()
for _ in range(int(input())):
    lst.add(input().rstrip())
for i in sorted(lst, key=lambda x: (len(x), x)):
    print(i)