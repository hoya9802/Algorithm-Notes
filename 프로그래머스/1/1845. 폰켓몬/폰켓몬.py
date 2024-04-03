from collections import Counter

def solution(nums):
    answer = 0
    a = Counter(nums)
    pick_num = len(nums)//2
    if pick_num >= len(a):
        return len(a)
    else:
        return pick_num