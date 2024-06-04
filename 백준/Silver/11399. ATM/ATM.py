import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

lst.sort()
res = 0; temp = 0
for i in lst:
    temp += i
    res += temp
print(res)