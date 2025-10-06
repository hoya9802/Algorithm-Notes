def checker(uid, bid):
    if len(uid) != len(bid):
        return False
    for u, b in zip(uid, bid):
        if b != "*" and u != b:
            return False
    else:
        return True

def solution(user_id, banned_id):
    ans = set()
    
    def dfs(idx, v):
        if idx == len(banned_id):
            ans.add(frozenset(v))
            return
        
        for i in range(len(user_id)):
            if user_id[i] not in v and checker(user_id[i], banned_id[idx]):
                dfs(idx+1, v+[user_id[i]])
    
    dfs(0, [])
    
    return len(ans)