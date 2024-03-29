def dis_cal(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return (abs(x1-x2) + abs(y1-y2))

def find_index(number, pad):
    index = []
    for i in range(len(pad)):
        for j in range(len(pad[0])):
            if number == pad[i][j]:
                index.append(i)
                index.append(j)
    return index

def solution(numbers, hand):
    answer = ''
    left_pos = [3,0]; right_pos = [3,2]
    key_pad = [[1,2,3],
              [4,5,6],
              [7,8,9],
              ['*',0,'#']]
    current_loc = {'left':left_pos, 'right':right_pos}
    
    for number in numbers:
        if number in [1,4,7]:
            answer += 'L'
            current_loc['left'] = find_index(number,key_pad)
        elif number in [3,6,9]:
            answer += 'R'
            current_loc['right'] = find_index(number,key_pad)
        else:
            if dis_cal(current_loc['left'], find_index(number,key_pad)) < dis_cal(current_loc['right'], find_index(number,key_pad)):
                answer += 'L'
                current_loc['left'] = find_index(number,key_pad)
            elif dis_cal(current_loc['left'], find_index(number,key_pad)) > dis_cal(current_loc['right'], find_index(number,key_pad)):
                answer += 'R'
                current_loc['right'] = find_index(number,key_pad)
            else:
                if hand == "right":
                    answer += 'R'
                    current_loc['right'] = find_index(number,key_pad)
                else:
                    answer += 'L'
                    current_loc['left'] = find_index(number,key_pad)
    print(answer)
    return answer