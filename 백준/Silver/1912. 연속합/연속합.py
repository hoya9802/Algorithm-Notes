import  sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
for i in range(1,n):
    lst[i] = max(lst[i-1]+lst[i], lst[i])
print(max(lst))