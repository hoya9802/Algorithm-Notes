# my solution
def solution(survey, choices):
    score_board = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    score = [3, 2, 1, 0, 1, 2, 3]
    
    for tp, choice in zip(survey, choices):
        idx = [x for x in tp]
        if choice >= 4:
            score_board[idx[-1]] += score[choice-1]
        else:
            score_board[idx[0]] += score[choice-1]
    answer = ''
    if score_board['R'] >= score_board['T']:
        answer += 'R'
    else:
        answer += "T"
        
    if score_board['C'] >= score_board['F']:
        answer += 'C'
    else:
        answer += "F"
        
    if score_board['J'] >= score_board['M']:
        answer += 'J'
    else:
        answer += "M"
        
    if score_board['A'] >= score_board['N']:
        answer += 'A'
    else:
        answer += "N"
        
    return answer