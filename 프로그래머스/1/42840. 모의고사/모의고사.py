def solution(answers):
    answer = [0,0,0]
    math_idiot = {1:[1, 2, 3, 4, 5], 2:[2, 1, 2, 3, 2, 4, 2, 5], 3:[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]}
    ans_len = len(answers)
    for n in math_idiot.keys():
        for x, y in zip(math_idiot[n] * (ans_len//len(math_idiot[n])) + math_idiot[n][:ans_len%len(math_idiot[n])], answers):
            if x == y:
                answer[n-1] += 1
    mx_val = max(answer)
    res = []
    for idx, i in enumerate(answer):
        if i == mx_val:
            res.append(idx+1)

    return res