# solve 2
def solution(s):
    number_name = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    for n in number_name:
        if n in s:
            s = s.replace(n, str(number_name[n]))

    return int(s)