import sys
input = sys.stdin.readline

n, s = map(int, input().split())
data = [0]+list(map(int, input().split()))

for i in range(1,len(data)):
    data[i] += data[i-1]

pointer = 0; res = 100_000
for i in range(len(data)):
    if data[i] < s:
        continue
    while pointer < i:
        temp = data[i] - data[pointer]
        if temp >= s:
            if res > i - pointer:
                res = i - pointer
        else:
            break
        pointer += 1
if res == 100_000:
    print(0)
else:
    print(res)