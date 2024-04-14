def solution(phone_book):
    answer = True
    data = sorted(phone_book)
    for i in range(len(data)-1):
        if data[i+1].startswith(data[i]):
            return False

    return answer