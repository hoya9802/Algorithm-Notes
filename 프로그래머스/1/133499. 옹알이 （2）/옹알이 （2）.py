def solution(babbling):
    answer = 0
    res = []
    for bab in babbling:
        pos_babbling = ['aya', 'ye', 'woo', 'ma']
        check_box = [0,0,0,0]
        temp = ''
        for word in bab:
            temp += word
            if temp in pos_babbling and check_box[pos_babbling.index(temp)] == 0:
                check_box = [0,0,0,0]
                check_box[pos_babbling.index(temp)] = 1
                temp = ''
        if len(temp) == 0:
            answer += 1
    
    return answer