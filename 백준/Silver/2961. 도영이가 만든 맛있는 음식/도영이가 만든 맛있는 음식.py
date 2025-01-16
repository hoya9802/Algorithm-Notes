import sys
input = sys.stdin.readline

n = int(input())
ingred = [list(map(int, input().split())) for _ in range(n)]

res = float('inf')

def dfs(idx, current_s, current_b, count):
    global res
    
    # 종료 조건: 모든 재료를 탐색했을 때
    if idx == n:
        # 하나 이상의 재료를 사용한 경우에만 계산
        if count > 0:
            res = min(res, abs(current_s - current_b))
        return

    # 1. 현재 재료를 선택한 경우
    dfs(idx + 1, current_s * ingred[idx][0], current_b + ingred[idx][1], count + 1)

    # 2. 현재 재료를 선택하지 않은 경우
    dfs(idx + 1, current_s, current_b, count)

# 초기 상태: 신맛=1, 쓴맛=0, 선택한 재료 수=0
dfs(0, 1, 0, 0)
print(res)
