import sys
input = sys.stdin.readline

n = int(input())

lst = set()
for _ in range(n):
    lst.add(input().rstrip())

print('\n'.join(sorted(lst, key=lambda x: (len(x), x))))
