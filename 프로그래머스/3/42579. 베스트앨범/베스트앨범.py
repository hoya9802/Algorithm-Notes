def solution(genres, plays):
    ans = {}; res = []
    for i in range(len(genres)):
        if genres[i] in ans:
            ans[genres[i]]['t'] += plays[i]
            ans[genres[i]]['l'].append((plays[i], i))
            continue
        ans[genres[i]] = {'t':plays[i], 'l':[(plays[i], i)]}
    
    ans = list(ans.values())
    ans.sort(key=lambda x:x['t'], reverse=True)
    
    for i in ans:
        tmp = sorted(i['l'], key=lambda x: x[0], reverse=True)
        for j in range(2 if len(tmp) >= 2 else len(tmp)):
            res.append(tmp[j][-1])
            
    return res