def solution(n):
    answer = 0
    check = 1
    while check <= n:
        temp = 0
        for i in range(check, n+1):
            temp += i
            if temp == n:
                answer += 1; check += 1
                break
            if temp > n:
                check += 1
                break
                
    return answer