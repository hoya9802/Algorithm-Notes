import sys
input = sys.stdin.readline

n = int(input())

lst = sorted(list(map(int, input().split())))

left, right = 0, n-1

ans = abs(lst[left] + lst[right])
final = [lst[left], lst[right]]

while left < right:
    tmp = lst[left] + lst[right]

    if abs(tmp) < ans:
        ans = abs(tmp)
        final = [lst[left], lst[right]]
        if ans == 0:
            break

    if tmp < 0:
        left += 1
    else:
        right -= 1

print(*final)