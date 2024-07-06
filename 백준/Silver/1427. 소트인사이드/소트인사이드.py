import sys
input = sys.stdin.readline

n = str(input().rstrip())
lst = []
for i in n:
    lst.append(i)
lst.sort(reverse=True)
print(''.join(lst))