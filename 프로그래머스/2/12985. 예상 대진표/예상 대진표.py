import math

def solution(n,a,b):
    i = 1
    while i <= int(math.log(n,2)):
        a, b = (a+1)//2, (b+1)//2
        if a == b:
            return i
        i += 1