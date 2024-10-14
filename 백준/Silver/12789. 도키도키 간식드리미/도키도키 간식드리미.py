import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
temp = []; target = 1
for i in range(n):
    temp.append(arr[i])
    while temp and target == temp[-1]:
        target += 1
        temp.pop()

print('Nice' if not temp else 'Sad')