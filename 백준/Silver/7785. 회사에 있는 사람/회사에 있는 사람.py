import sys
input = sys.stdin.readline

room = {}
for _ in range(int(input())):
    a, b = input().split()
    if b == 'enter':
        room[a] = 'enter'
    if b == 'leave' and room[a] == 'enter':
        room.pop(a)

print(*sorted([i for i in room.keys()], reverse=True), sep='\n')