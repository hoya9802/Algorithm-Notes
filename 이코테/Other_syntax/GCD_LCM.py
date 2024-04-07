import math

print('15와 35의 최대공약수:',math.gcd(15, 35)) # python built-in-function

def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n%m)
    
print('15와 35의 최대공약수:',gcd(15, 35))

def lcm(n, m):
    tmp = gcd(n, m)
    return (n*m) // tmp

print('25와 30의 최소공배수:',lcm(25,30))