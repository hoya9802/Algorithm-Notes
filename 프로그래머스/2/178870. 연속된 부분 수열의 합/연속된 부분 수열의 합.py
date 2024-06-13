# solve 6

def solution(sequence, k):
    end, interval_sum = 0, 0; first, second = 0, 1000001
    for start in range(len(sequence)):
        while end < len(sequence) and interval_sum < k:
            interval_sum += sequence[end]
            end += 1
        if interval_sum == k and second - first > (end-1) - start:
            first, second = start, end -1
        interval_sum -= sequence[start]
    return [first, second]