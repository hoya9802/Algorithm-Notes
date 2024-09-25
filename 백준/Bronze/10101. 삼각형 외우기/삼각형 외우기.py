import sys
input = sys.stdin.readline

res = [int(input()) for _ in range(3)]
if sum(res) == 180:
    if res.count(60) == 3:   print('Equilateral')
    elif len(set(res)) == 2: print('Isosceles')
    else:                    print('Scalene')
else:                        print('Error')