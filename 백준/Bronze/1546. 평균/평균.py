n = int(input())
sl = list(map(int, input().split()))
mv = max(sl)
print(sum(x/mv*100 for x in sl)/n)