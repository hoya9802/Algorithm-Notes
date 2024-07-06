import sys
input = sys.stdin.readline

class solution:
    def __init__(self, y):
        self.y = sorted([x for x in y], reverse=True)

    def res(self):
        return ''.join(self.y)

a = solution(input().rstrip())
print(a.res())