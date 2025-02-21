import sys
input = sys.stdin.readline

n, m = map(int, input().split())

s = set([''.join(input().rsplit()) for _ in range(n)])

m = [''.join(input().rsplit()) for _ in range(m)]

print(sum([ 1 for i in m if i in s]))