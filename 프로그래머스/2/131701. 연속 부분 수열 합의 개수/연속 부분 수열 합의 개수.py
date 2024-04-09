# solve 1
def solution(elements):
    ans = set()
    for i in range(len(elements)):
        tmp = elements[i]
        ans.add(tmp)
        for j in range(i+1, i+len(elements)):
            tmp += elements[j%len(elements)]
            ans.add(tmp)
    
    return len(ans)