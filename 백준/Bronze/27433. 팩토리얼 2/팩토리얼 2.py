import sys

n = int(sys.stdin.readline())

def factorial(x):
    global res
    for i in range(1, x+1):
        res *= i
    return res

res = 1

if n == 0:
    print(1)
else:
    print(factorial(n))