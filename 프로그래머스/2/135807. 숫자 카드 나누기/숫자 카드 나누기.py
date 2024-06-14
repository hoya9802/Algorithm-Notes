def gcd(n, m):
    if m == 0:
        return n
    else: 
        return gcd(m, n%m)

def solution(arrayA, arrayB):
    gcd_a = arrayA[0]; gcd_b = arrayB[0]
    for a, b in zip(arrayA, arrayB):
        gcd_a = gcd(gcd_a, a)
        gcd_b = gcd(gcd_b, b)
        
    ans = 0
    for x in arrayA:
        if x % gcd_b == 0:
            break
    else:
         ans = gcd_b
            
    for x in arrayB:
        if x % gcd_a == 0:
            break
    else:
         ans = max(gcd_a, ans)
    return ans