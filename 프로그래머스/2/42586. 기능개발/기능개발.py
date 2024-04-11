def solution(progresses, speeds):
    res = [(100-pro)//sp if (100-pro)%sp==0 else (100-pro)//sp+1 for pro, sp in zip(progresses, speeds)]
    std, temp = 0, 1
    ans, stack = [], []
    for i in range(len(res)):
        if len(stack) == 0:
            std = i
            stack.append(res[i])
        else:
            if res[std] >= res[i]:
                temp += 1
                continue
            else:
                ans.append(temp)
                temp = 1
                std = i
                stack.append(res[i])
    ans.append(temp)  
    return  ans