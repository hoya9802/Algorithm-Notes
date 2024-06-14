def change_time(x):
    h,m = map(int, x.split(':'))
    return h*60+m

def solution(book_time):
    time_table = [0] * (24*60+10)
    res = 0
    for bt in book_time:
        s, e = bt
        time_table[change_time(s)] += 1
        time_table[change_time(e)+10] -= 1
    temp = 0
    for i in time_table:
        temp += i
        if temp > res:
            res = temp
    return res