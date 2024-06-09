def solution(k, dungeons):
    ans = 0    
    def dfs(k, c, dungeons, visited):
        nonlocal ans
        ans = max(ans, c)
        
        for i in range(len(dungeons)):
            if not visited[i] and k >= dungeons[i][0]:
                visited[i] = True
                dfs(k - dungeons[i][1], c+1, dungeons, visited)
                visited[i] = False
        
        
    visited = [False] * len(dungeons)
    dfs(k, 0, dungeons, visited)
    return ans