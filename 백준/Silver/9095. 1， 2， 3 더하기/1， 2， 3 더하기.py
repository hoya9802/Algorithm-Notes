import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    def top_down(num):
        if num == 1: return 1
        if num == 2: return 2
        if num == 3: return 4
        return top_down(num-1)+top_down(num-2)+top_down(num-3)
    print(top_down(n))