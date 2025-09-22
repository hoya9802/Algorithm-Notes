def solution(tickets):
    tick_dict = {}
    for s, e in tickets:
        if s not in tick_dict:
            tick_dict[s] = {'loc': [], 'visited': []}
        tick_dict[s]['loc'].append(e)
        tick_dict[s]['visited'].append(0)

    # 목적지 정렬 (사전순 우선 탐색 보장)
    for s in tick_dict:
        locs = tick_dict[s]['loc']
        visits = tick_dict[s]['visited']
        zipped = sorted(zip(locs, visits))
        tick_dict[s]['loc'], tick_dict[s]['visited'] = map(list, zip(*zipped))

    res = []

    def dfs(s, arr):
        if len(arr) == len(tickets) + 1:
            res.append(arr)
            return    

        for idx, e in enumerate(tick_dict.get(s, {'loc': []})['loc']):
            if tick_dict[s]['visited'][idx] == 1:
                continue
            tick_dict[s]['visited'][idx] = 1
            dfs(e, arr + [e])
            tick_dict[s]['visited'][idx] = 0

    dfs("ICN", ["ICN"])

    res.sort()
    return res[0]
