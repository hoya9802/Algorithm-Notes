def solution(x, y, n):
    INF = int(1e9)
    answer = [INF] * (y+1)
    answer[x]=0
    for i in range(x+1, y+1):
        if answer[i-n] >= 0:
            answer[i] = min(answer[i], answer[i-n] + 1)
        if i % 2 == 0 and answer[i//2] >= 0:
            answer[i] = min(answer[i], answer[i//2] + 1)
        if i % 3 == 0 and answer[i//3] >= 0:
            answer[i] = min(answer[i], answer[i//3] + 1)
    if answer[-1] == INF:
        return -1
    return answer[-1]