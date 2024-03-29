# my solution
def solution(n):
    n_3 = []
    while n>=1:
        n_3.append(n%3)
        n //= 3
    answer = 0
    for i, x in enumerate(n_3[::-1]):
        answer += (x * pow(3,i))
    return answer

# best solution
# def solution(n):
#     tmp = ''
#     while n:
#         tmp += str(n % 3)
#         n = n // 3

#     answer = int(tmp, 3) # int(num, 3) -> 3진법인 str형태의 tmp을 10진법으로 변경
#     return answer