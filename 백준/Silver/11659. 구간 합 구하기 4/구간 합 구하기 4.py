import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
psum = [0] * (n+1)
for i in range(1, n+1):
    psum[i] = data[i-1] + psum[i-1]

for _ in range(m):
    s, e = map(int, input().split())
    print(psum[e]-psum[s-1])