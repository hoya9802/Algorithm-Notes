def solution(n):
    ans = 0
    v1 = [0] * n
    v2 = [0] * (2*n)
    v3 = [0] * (2*n)
    
    def dfs(v):
        nonlocal ans
        if v == n:
            ans += 1
            return
        for i in range(n):
            if v1[i] == v2[v-i] == v3[v+i] == 0:
                v1[i] = v2[v-i] = v3[v+i] = 1
                dfs(v+1)
                v1[i] = v2[v-i] = v3[v+i] = 0
    dfs(0)
    return ans