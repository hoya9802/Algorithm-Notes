import sys
input = sys.stdin.readline

while 1:
    length = sorted(map(int, input().split()))
    if sum(length) == 0:
        break
    if length[-1] >= sum(length[:2]):
        print("Invalid")
        continue
    checker = len(set(length))
    if checker == 1:
        print('Equilateral')
    elif checker == 2:
        print('Isosceles')
    else:
        print('Scalene')