from collections import defaultdict

# my solution
def solution(friends, gifts):
    score = defaultdict(int)
    combi = defaultdict(int)

    for friend in friends:
        score[friend] = 0

    for record in gifts:
        giver, taker = record.split()
        combi[(giver, taker)] += 1
        score[giver] += 1
        score[taker] -= 1
    
    ans = -1
    for i in friends:
        temp = 0
        for j in friends:
            if i == j:
                continue
            if combi[(i, j)] > combi[(j,i)]:
                temp += 1
            if combi[(i, j)] == combi[(j, i)] and score[i] > score[j]:
                temp += 1
        ans = max(ans, temp)
    
    return ans

# best solution
def solution(friends, gifts):
    f = {v: i for i, v in enumerate(friends)}
    l = len(friends)
    p = [0] * l
    answer = [0] * l
    gr = [[0] * l for i in range(l)]
    for i in gifts:
        a, b = i.split()
        gr[f[a]][f[b]] += 1
    for i in range(l):
        p[i] = sum(gr[i]) - sum([k[i] for k in gr])

    for i in range(l):
        for j in range(l):
            if gr[i][j] > gr[j][i]:
                answer[i] += 1
            elif gr[i][j] == gr[j][i]:
                if p[i] > p[j]:
                    answer[i] += 1
    return max(answer)