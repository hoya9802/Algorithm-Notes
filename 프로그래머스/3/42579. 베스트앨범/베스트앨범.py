def solution(genres, plays):
    res = {}
    idx = 0
    for g, p in zip(genres, plays):
        if g not in res.keys():
            res[g] = {'t':0, 'id':[]}
        res[g]['t'] += p; res[g]['id'].append((p, idx))
        idx += 1
            
    lst = sorted(list(x for x in res.values()), key=lambda x:x['t'], reverse=True)
    lst = list(sorted(x['id'], key=lambda x:x[0], reverse=True) for x in lst)
    ans = []
    for i in lst:
        for j in range(2 if len(i) > 2 else len(i)):
            ans.append(i[j][-1])
    return ans