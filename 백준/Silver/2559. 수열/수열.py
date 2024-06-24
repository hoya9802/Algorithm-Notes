import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data_temp = list(map(int, input().split()))

temp = 0
for i in range(k):
    temp += data_temp[i]
ans = -int(1e9)
if ans < temp:
    ans = temp

for i in range(1, n-k+1):
    temp += data_temp[i+k-1]
    temp -= data_temp[i-1]
    if ans < temp:
        ans = temp
print(ans)