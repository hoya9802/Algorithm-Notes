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
    stack = deque()
    
    for i in range(len(arr)):
        stack.append(arr[i])
        if len(stack) == 2:
            stack.append(find_lcm(stack[0], stack[1]))
            stack.popleft(); stack.popleft()
    return stack[0]
