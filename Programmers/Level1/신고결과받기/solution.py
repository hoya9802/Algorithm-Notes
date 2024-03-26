# my solution
def solution(id_list, report, k):
    l = len(id_list)
    name_to_number = {n: i for i, n in enumerate(id_list)}
    data = [[0] * l for _ in range(l)]
    for i in report:
        giver, taker = i.split()
        if data[name_to_number[giver]][name_to_number[taker]] == 0:
            data[name_to_number[giver]][name_to_number[taker]] += 1
    r = [0] * l
    for i in range(l):
        r[i] = sum([x[i] for x in data])

    ban = [i for i, v in enumerate(r) if v >= k]
    answer = [0] * l
    for i in range(l):
        answer[i] = sum([x for i, x in enumerate(data[i]) if i in ban])

    return answer

# best solution
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    data = {v:0 for v in id_list}
    for i in set(report):
        data[i.split()[1]] += 1
    for i in set(report):
        if data[i.split()[1]] >= k:
            answer[id_list.index(i.split()[0])] += 1
    return answer