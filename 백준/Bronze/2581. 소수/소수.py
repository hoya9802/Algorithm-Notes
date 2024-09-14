import math, sys
input = sys.stdin.readline

def check(x):
    if x == 1: return 0
    elif x == 2: return 1
    else:
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0:
                return 0
        else:
            return 1
        
res = [x for x in range(int(input()), int(input())+1) if check(x)]
try:
    print(sum(res), res[0], sep='\n')
except IndexError as index:
    print(-1)