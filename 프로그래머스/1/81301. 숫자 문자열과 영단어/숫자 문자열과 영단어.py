def solution(s):
    num_word = {'zero':"0", 'one':"1", 'two':"2", 'three':"3", 'four':"4", 'five':"5", 'six':"6",
               'seven':"7", 'eight':"8", 'nine':"9"}
    for i in num_word:
        if i in s:
            s = s.replace(i, str(num_word[i]))
    return int(s)