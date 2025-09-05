def solution(genres, plays):
    data = {}

    for i in range(len(genres)):
        if not genres[i] in data:
            data[genres[i]] = {'t':0, 'l':[]}
        data[genres[i]]['l'].append({'v': plays[i],'id': i})
        data[genres[i]]['t'] += plays[i]

    data = list(data.values())
    data.sort(key=lambda x: x['t'], reverse=True)

    ans = []
    for i in range(len(data)):
        tmp = sorted(data[i]['l'], key=lambda x:x['v'], reverse=True)
        for j in range(2 if len(tmp) >= 2 else len(tmp)):
            ans.append(tmp[j]['id'])

    return ans