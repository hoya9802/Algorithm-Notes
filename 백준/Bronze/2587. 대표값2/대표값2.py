res = []
for _ in range(5):
    res.append(int(input()))
print(sum(res)//5, sorted(res)[2], sep='\n')