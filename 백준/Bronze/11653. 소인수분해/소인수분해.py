import math

def check(x):
    if x == 1: return 0
    elif x == 2: return 1
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return 0
    else:
        return 1

n = int(input())
if n == 1:
    exit()
res = []
while not check(n):
    for i in range(2, int(math.sqrt(n))+1):
        if check(i) and n % i == 0:
            res.append(i)
            break
    n //= i
res.append(n)
print(*res, sep='\n')