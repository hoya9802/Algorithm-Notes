import sys, math

while 1:
    n = int(sys.stdin.readline())
    if n == -1:
        break
    res = []
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            res.append(i)
            res.append(n//i)
    if n == sum(sorted(res)[:-1]):
        print(f"{n} = {' + '.join(map(str, sorted(res)[:-1]))}")
    else:
        print(f'{n} is NOT perfect.')