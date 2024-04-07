from collections import deque

def find_lcm(x, y):
    ans = 1
    max_val = max(x,y); min_val = min(x,y)
    stack = list();
    i = 2  
    while min_val >= i:
        if max_val % i == 0 and min_val % i == 0:
            max_val //= i; min_val //= i
            stack.append(i)
        else:
            i += 1 

    stack.append(max_val); stack.append(min_val)
    
    for i in stack:
        ans *= i
    return ans
        
def solution(arr):
    ans = arr[0]
    
    for i in arr[1:]:
        t = find_lcm(ans, i)
        ans = t
    
    return ans