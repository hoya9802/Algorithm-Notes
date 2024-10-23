import sys
input = sys.stdin.readline

words = input().rstrip()
bomb = input().rstrip()
l = len(bomb)

res = []
for i in words:
    res.append(i)
    if len(res) >= l and ''.join(res[len(res)-l::]) == bomb:
        del res[len(res)-l::]

print(''.join(res) if res else 'FRULA')