print('생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.')
n, target = input().split()
print('앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 듸어쓰기 한 칸으로 합니다.')
array = list(input().split())

def sequential_search(n, target):
    for i in range(int(n)):
        if array[i] == target:
            return i + 1

print(sequential_search(n, target))

"""
생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.
5 ian
앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 듸어쓰기 한 칸으로 합니다.
hanul zerus cris jelly ian
output: 5
"""