n, b = map(int, input().split())

res = []
while n!=0:
    ans = n%b
    if ans >= 10:
        ans = chr(ans+55)
    res.append(str(ans))
    n //= b

print(''.join(res[::-1]))