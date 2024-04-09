def solution(clothes):
    ans=1
    clodict = {}
    for i in clothes:
        clodict[i[-1]]=0
    
    for k in clothes:
        clodict[k[-1]]+=1
        
    for h in clodict.values():
        ans=(h+1)*ans
        
    return ans-1