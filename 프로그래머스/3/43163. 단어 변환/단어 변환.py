def checker(a, b):
    count = 0
    for i, j in zip(a, b):
        if i != j:
            count += 1
    return count

def solution(begin, target, words):
    if target not in words: return 0
    ans = int(1e9)
    
    def dfs(curr, target, count, visited):
        nonlocal ans
        if curr == target:
            if ans > count:
                ans = count
            return
        
        for i in range(len(words)):
            if visited[i] != 0:
                continue
            else:
                if checker(curr, words[i]) == 1:
                    visited[i] = 1
                    dfs(words[i], target, count+1, visited)
                    visited[i] = 0
                    
    for i in range(len(words)):
        visited = [0] * len(words)
        if checker(begin, words[i]) == 1:
            visited[i] = 1
            dfs(words[i], target, 1, visited)
            visited[i] = 0
            
    return ans