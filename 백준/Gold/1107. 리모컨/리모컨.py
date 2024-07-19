import sys
input = sys.stdin.readline

ch = int(input())
n = int(input())
del_num = list(map(int, input().split()))

res = abs(ch - 100)

for i in range(ch + res):
    num = list(str(i))
    for j in num:
        if int(j) in del_num:
            break
    else:
        res = min(res, abs(ch-i) + len(num))

print(res)