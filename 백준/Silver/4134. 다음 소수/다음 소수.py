import sys
input = sys.stdin.readline

def checker(x):
    check = True
    for i in range(2, int(x**(1/2))+1):
        if x % i == 0:
            check = False
            break
    return check


for _ in range(int(input())):
    s = int(input())
    if s <= 1: print(2); continue
    while 1:
        if checker(s):
            print(s)
            break
        else:
            s += 1
