def solution(numbers, target):
    ans = 0

    def dfs(sm, idx):
        nonlocal ans
        if idx == len(numbers):
            if sm == target:
                ans += 1
            return
        else:
            dfs(sm + numbers[idx], idx + 1)
            dfs(sm - numbers[idx], idx + 1)

    dfs(0, 0)
    return ans
