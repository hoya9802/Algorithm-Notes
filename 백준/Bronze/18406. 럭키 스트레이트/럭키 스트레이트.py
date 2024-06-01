n = input()
left = n[:len(n)//2]; right = n[len(n)//2:]
if sum(int(l) for l in left) == sum(int(r) for r in right):
    print('LUCKY')
else:
    print('READY')