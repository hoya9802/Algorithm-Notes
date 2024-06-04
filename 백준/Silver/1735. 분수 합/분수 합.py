import sys
input = sys.stdin.readline

fs, fm = map(int, input().split())
ss, sm = map(int, input().split())

def gcd(n, m):
    if m == 0:
        return n
    else: 
        return gcd(m, n%m)

lcm = fm * sm // gcd(fm, sm)
top = (fs * lcm//fm) + (ss * lcm//sm)
ltd = gcd(lcm, top)
print(top//ltd, lcm//ltd)