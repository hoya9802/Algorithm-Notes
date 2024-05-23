def solution(n):
    global ans
    ans = 0
    v1 = [0] * n
    v2 = [0] * (2*n)
    v3 = [0] * (2*n)
    
    def dfs(start):
        global ans
        if start == n:
            ans += 1
            return 
        for i in range(n):
            if v1[i] == v2[i+start] == v3[start-i] == 0:
                v1[i] = v2[i+start] = v3[start-i] = 1
                dfs(start+1)
                v1[i] = v2[i+start] = v3[start-i] = 0

    dfs(0)
    return ans