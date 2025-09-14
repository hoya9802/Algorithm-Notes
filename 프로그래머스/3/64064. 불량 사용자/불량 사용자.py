def matches(user, ban):
    if len(user) != len(ban):
        return False
    for u, b in zip(user, ban):
        if b != '*' and u != b:
            return False
    return True

def solution(user_id, banned_id):
    ans = set()

    def dfs(idx, chosen):
        if idx == len(banned_id):
            ans.add(frozenset(chosen))
            return
        for u in user_id:
            if u not in chosen and matches(u, banned_id[idx]):
                dfs(idx + 1, chosen + [u])

    dfs(0, [])
    return len(ans)
