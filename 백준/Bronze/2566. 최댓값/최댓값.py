lst = [list(map(int, input().split())) for _ in range(9)]

res=-1
for i in range(9):
    for j in range(9):
        if lst[i][j] > res:
            res = lst[i][j]
            x=i; y=j

print(res)
print(x+1,y+1)