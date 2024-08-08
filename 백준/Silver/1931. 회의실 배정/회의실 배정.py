import sys
input = sys.stdin.readline

n = int(input())
lst = []

for _ in range(n):
    a, b = map(int, input().split())
    lst.append((a,b))

lst.sort(key=lambda x:(x[-1], x[0]))
end = lst[0][1]
count = 1
for i in range(1,n):
    if end <= lst[i][0]:
        end = lst[i][1]
        count += 1

print(count)