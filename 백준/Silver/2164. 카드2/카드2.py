import sys
from collections import deque
input = sys.stdin.readline

lst = deque([x for x in range(1, int(input())+1)])

while len(lst) != 1:
    lst.popleft()
    lst.append(lst.popleft())
print(lst[0])