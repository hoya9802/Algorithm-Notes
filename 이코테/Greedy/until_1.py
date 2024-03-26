n, k = map(int, input().split())

result = 0
while 1:
    target = (n // k) * k
    result += (n - target)

    if n < k:
        result -= 1 # result에 n - target를 하는 과정은 0으로 만드는 과정이기 때문에 마지막 횟수는 제외
        break
    n //= k
    result += 1

print(result)
"""
input: 25, 5
output: 2
"""