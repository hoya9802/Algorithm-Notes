N = int(input())
lst = list(map(int, input().split()))
target = int(input())
print(sum(1 for x in lst if x == target))