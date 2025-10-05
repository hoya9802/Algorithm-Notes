def solution(sticker):
    n = len(sticker)
    dp1 = [0] * n; dp2 = [0] * n
    
    for i in range(n):
        if i == 0:
            dp1[0] = sticker[0]
            continue
        dp1[i] = max(dp1[i-1], dp1[i-2]+sticker[i])
        dp2[i] = max(dp2[i-1], dp2[i-2]+sticker[i])
    
    if n == 1:
        return dp1[0]
    
    return max(dp1[-2], dp2[-1])