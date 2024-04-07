def find_lcm(x, y):
    if y == 0:
        return x
    else:
        return find_lcm(y, x%y)
        
def solution(arr):
    ans = arr[0]
    
    for i in arr[1:]:
        t = ans * i // find_lcm(ans, i)
        ans = t
    
    return ans