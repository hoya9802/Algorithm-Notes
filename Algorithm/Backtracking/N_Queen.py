## 문제 설명 
## 가로, 세로 길이가 n인 정사각형으로된 체스판이 있습니다. 체스판 위의 n개의 퀸이 서로를 공격할 수 없도록 배치하고 싶습니다.
## 예를 들어서 n이 4인경우 다음과 같이 퀸을 배치하면 n개의 퀸은 서로를 한번에 공격 할 수 없습니다.

N = int(input())
ans = 0
v1 = [0] * N
v2 = [0] * (2*N)
v3 = [0] * (2*N)

def dfs(n):
    global ans
    if n == N:
        ans += 1
        return
    for i in range(N):
        if v1[i] == v2[n+i] == v3[n-i] == 0:
            v1[i] = v2[n+i] = v3[n-i] = 1
            dfs(n+1)
            v1[i] = v2[n+i] = v3[n-i] = 0

dfs(0)
print(ans)