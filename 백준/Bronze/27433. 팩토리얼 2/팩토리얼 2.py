import sys

n = int(sys.stdin.readline())

def factorial(x):
    if x in (0,1):
        return 1
    return x * factorial(x-1)

print(factorial(n))