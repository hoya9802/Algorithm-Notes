def solution(sizes):
    max_values = []; min_values = []
    for i in sizes:
        max_values.append(max(i))
        min_values.append(min(i))
    
    return max(max_values) * max(min_values)