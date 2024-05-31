n, m = map(int, input().split())
lst = [x for x in range(1, n+1)]
for _ in range(m):
    s, e = map(int, input().split())
    lst[s-1:e] = lst[s-1:e][::-1]
for i in lst:
    print(i, end=" ")