arr = []; l = 0
for _ in range(5):
    tmp = list(input())
    arr.append(tmp)
    if l < len(tmp):
        l = len(tmp)

for i in range(l):
    for j in range(5):
        try:
            print(arr[j][i], end="")
        except:
            continue