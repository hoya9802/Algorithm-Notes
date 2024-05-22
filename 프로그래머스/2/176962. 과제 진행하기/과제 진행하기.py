def time_change(x):
    h, m = map(int, x.split(':'))
    return h * 60 + m

def solution(plans):
    ans = []
    plans.sort(key=lambda x: x[1])
    stack = []
    for i in range(len(plans)):
        left_time = 0
        sb, time, use = plans[i]
        if i + 1 >= len(plans):
            ans.append(sb)
            break
        if time_change(time) + int(use) > time_change(plans[i+1][1]):
            stack.append([sb, time_change(time)+int(use) - time_change(plans[i+1][1])])
        elif time_change(time) + int(use) <= time_change(plans[i+1][1]):
            left_time = time_change(plans[i+1][1]) - (time_change(time) + int(use))
            ans.append(sb)
            if left_time > 0:
                while stack and left_time > 0:
                    temp_sub, temp_time = stack.pop()
                    if temp_time <= left_time:
                        ans.append(temp_sub)
                        left_time -= temp_time
                    else:
                        temp_time -= left_time
                        stack.append([temp_sub, temp_time])
                        break
    while stack:
        temp_sub, temp_time = stack.pop()
        ans.append(temp_sub)
    return ans