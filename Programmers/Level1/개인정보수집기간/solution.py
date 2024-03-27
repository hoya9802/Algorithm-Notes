# my solution
def solution(today, terms, privacies):
    date = [int(x) for x in today.split('.')]
    terms_data = dict()
    for term in terms:
        record_type, period = term.split()
        terms_data[record_type] = int(period)
    pri = []
    for i in privacies:
        y,m,dt = i.split('.')
        d, t = dt.split()
        pri.append([int(y),int(m),int(d),t])
    result = []
    for i in pri:
        y = (date[0] - i[0]) * (12 * 28)
        m = (date[1] - i[1]) * (28)
        d = (date[2] - i[2])
        t = terms_data[i[-1]] * (28)
        result.append([y+m+d,t])
    answer = [i+1 for i in range(len(result)) if result[i][0] >= result[i][1]]
    
    return answer

# best solution
def to_days(date):
    year, month, day = map(int, date.split("."))
    return year * 28 * 12 + month * 28 + day

def solution(today, terms, privacies):
    months = {v[0]: int(v[2:]) * 28 for v in terms}
    today = to_days(today)
    expire = [
        i + 1 for i, privacy in enumerate(privacies)
        if to_days(privacy[:-2]) + months[privacy[-1]] <= today
    ]
    return expire
