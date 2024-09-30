n = int(input())

for i in range(1,n):
    temp = sum([int(x) for x in str(i)])
    if temp + i == n:
        print(i)
        break
else:
    print(0)