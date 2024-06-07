import sys

input = sys.stdin.readline
lst = list(map(int, input().split()))
lst = [x**2 for x in lst]
print(sum(lst)%10)