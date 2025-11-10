def convert_time(x):
    h = x // 60
    m = x % 60
    if h < 10:
        h = "0"+str(h)
    if m < 10:
        m = "0"+str(m)
    return str(h)+":"+str(m)

def solution(n, t, m, timetable):
    shuttles = [[] for _ in range(n)]
    depart_time = [540+i*t for i in range(n)]
    
    time_table = []
    for time in sorted(timetable):
        hh, mm = map(int, time.split(":"))
        time_table.append(hh*60+mm)
        
    idx_human = 0
    for idx, now in enumerate(depart_time):
        count = 0
        while count < m and (idx_human < len(timetable) and time_table[idx_human] <= now):
            shuttles[idx].append(idx_human)
            idx_human += 1
            count += 1
    
    if len(shuttles[-1]) < m:
        return convert_time(depart_time[-1])
    return convert_time(time_table[shuttles[-1][-1]]-1)