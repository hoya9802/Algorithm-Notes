answer = 0
def dfs(i, total, numbers, target):
    global answer
    if i == len(numbers):
        if total == target:
            answer += 1
        return
    dfs(i+1, total+numbers[i], numbers, target)
    dfs(i+1, total-numbers[i], numbers, target)

def solution(numbers, target):
    dfs(0, 0, numbers, target)
    return answer