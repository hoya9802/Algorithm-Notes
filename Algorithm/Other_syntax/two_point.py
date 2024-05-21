# 리스트에 음수가 있으면 two-point 사용불가
# input = [1,2,3,2,5] / m = 5 일때의 개수

a = [1,2,3,2,5]
m = 5
n = len(a)

e, res  = 0, 0
interval_sum = 0
for start in range(n):
    while e < n and interval_sum < m:
        interval_sum += a[e]
        e += 1
    if m == interval_sum:
        res += 1

    interval_sum -= a[start]

print(res)

# 서로 다른 크기를 가지는 2개의 리스트가 주어졌을때 두 리스중 작은 값을 가리키는 코드
n, m = 3, 4
a = [1, 3, 5]
b = [2, 4, 6, 8]

res = [0] * (n+m)
i, j, k = 0, 0, 0

while i < n or j < m:
    if j >= m or (i < n and a[i] < b[j]):
        res[k] = a[i]
        i += 1
    else:
        res[k] = b[j]
        j += 1
    k += 1

for i in res:
    print(i, end=" ")