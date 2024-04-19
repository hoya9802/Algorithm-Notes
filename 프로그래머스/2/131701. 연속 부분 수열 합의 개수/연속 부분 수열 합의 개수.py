# solve 1

def solution(elements):
    ans = set()
    for i in range(len(elements)):
        temp = elements[i]
        ans.add(temp)
        for j in range(1+i, len(elements)+i):
            temp += elements[j%len(elements)]
            ans.add(temp)

    return len(ans)