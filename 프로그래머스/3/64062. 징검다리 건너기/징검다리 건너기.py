def canCross(stones, k, people):
    count = 0
    for stone in stones:
        if stone < people:
            count += 1
            if count >= k:
                return False
        else:
            count = 0
    return True


def solution(stones, k):
    left, right = 1, max(stones)
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        if canCross(stones, k, mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer
