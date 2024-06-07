import sys
input = sys.stdin.readline

n = input().rstrip()

cnt = [0] * 11

for i in n:
    num = int(i)
    if num == 6 or num == 9:
        if cnt[6] < cnt[9]:
            cnt[6] += 1
        else:
            cnt[9] += 1
        continue
    else:
        cnt[num] += 1
print(max(cnt))