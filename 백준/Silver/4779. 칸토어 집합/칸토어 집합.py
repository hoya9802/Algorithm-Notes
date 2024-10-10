import sys, math
input = sys.stdin.readline

def CantorSet(x):
    if len(x) <= 1:
        return x
    l = len(x)//3
    return CantorSet('-'*l) + ' '*l + CantorSet('-'*l)

while 1:
    try:
        n = int(input())
        line = '-' * (3**n)
        print(CantorSet(line))
    except:
        break