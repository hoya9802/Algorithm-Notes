def solution(tickets):
    l = len(tickets)+1
    ticket_dict = {}
    for t in tickets:
        if t[0] not in ticket_dict:
            ticket_dict.update({t[0]:[t[1]]})
            continue
        ticket_dict[t[0]].append(t[1])
        
    for t in tickets:
        ticket_dict[t[0]].sort()

    ans = []
    def dfs(v, lst):
        if len(lst) == l:
            ans.append(lst)
            return
        
        if v not in ticket_dict:
            return
        
        for idx, i in enumerate(ticket_dict[v]):
            ticket_dict[v].pop(idx)
            dfs(i, lst+[i])
            ticket_dict[v].insert(idx, i)

    dfs('ICN', ['ICN'])
    return ans[0]