# my solution
def solution(bandage, health, attacks):
    max_time = 0
    for i in attacks:
        max_time = max(max_time, i[0])
    hp = health
    c = 0
    demage_index = 0
    for time in range(max_time+1):
        if hp >= health:
            hp = health
        if time in [i[0] for i in attacks]:
            demage = [i[1] for i in attacks]
            hp -= demage[demage_index]
            demage_index += 1
            c = 0
            if hp <= 0:
                hp = -1
                break
            continue
        
        if hp >= health:
            continue
        else:
            hp += bandage[1]
            c += 1
            if c == bandage[0]:
                hp += bandage[-1]
                c = 0

    answer = hp
    
    return answer

# best solution
def solution(bandage, health, attacks):
    start = 1
    hp = health
    for time, demage in attacks:
        hp += (((time-start)//bandage[0]) * bandage[-1]) + ((time-start) * bandage[1])
        start = time+1
        if hp >- health:
            hp = health
        
        hp -= demage
        if hp <= 0:
            hp = -1
            break
    
    answer = hp
    return answer