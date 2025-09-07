def checker(user_id, banned_ids, banned_visited):
    for bi in range(len(banned_ids)):
        if banned_visited[bi] == 1 or len(user_id) != len(banned_ids[bi]):
            continue
        else:
            for u, b in zip(user_id, banned_ids[bi]):
                if b=="*" or u==b:
                    continue
                else:
                    break
            else:
                return bi    
    return 100

def solution(user_id, banned_id):
    ans=0
    user_visited = [0] * len(user_id)
    banned_visited = [0] * len(banned_id)
    
    tmp = []
    def dfs(user_id, banned_id, user_visited, banned_visited, arr):
        nonlocal tmp
        if len(arr) == len(banned_id):
            tmp.append(set(arr))
            return
        for i in range(len(user_id)):
            if user_visited[i] == 0:
                res = checker(user_id[i], banned_id, banned_visited)
                if res > 8:
                    continue
                user_visited[i] = 1
                banned_visited[res] = 1
                dfs(user_id, banned_id, user_visited, banned_visited, arr+[user_id[i]])
                user_visited[i] = 0
                banned_visited[res] = 0
                
    dfs(user_id, banned_id, user_visited, banned_visited, [])
    
    ans = len(set(map(frozenset, tmp)))
    return ans