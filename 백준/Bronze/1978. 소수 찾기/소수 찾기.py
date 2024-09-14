import math

def check(x):
    if x == 1: return 0
    elif x == 2: return 1
    else:
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0:
                return 0
        else:
            return 1
        
n = int(input())
print(sum([1 for i in list(map(int, input().split()))[:n] if check(i)]))