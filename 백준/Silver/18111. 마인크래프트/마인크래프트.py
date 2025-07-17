import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
graph = []

max_val, min_val = 0, int(1e9)
for _ in range(n):
    tmp_lst = list(map(int, input().split()))
    max_val = max(max_val, max(tmp_lst))
    min_val = min(min_val, min(tmp_lst))
    graph.append(tmp_lst)

min_time = int(1e9)
result_height = 0

for target_height in range(max_val, min_val-1, -1):
    blocks_needed = 0
    blocks_removed = 0
    time = 0
    
    for i in range(n):
        for j in range(m):
            current_height = graph[i][j]
            
            if current_height > target_height:
                diff = current_height - target_height
                blocks_removed += diff
                time += diff * 2
            elif current_height < target_height:
                diff = target_height - current_height
                blocks_needed += diff
                time += diff * 1
    
    available_blocks = b + blocks_removed
    if available_blocks >= blocks_needed:
        if time < min_time:
            min_time = time
            result_height = target_height

print(min_time, result_height)