import sys
input = sys.stdin.readline

n = int(input())
total = 2*n-1
for i in range(1,n+1):
    side = (total - (2*i-1))//2
    print(' '*side+'*'*(2*i-1))