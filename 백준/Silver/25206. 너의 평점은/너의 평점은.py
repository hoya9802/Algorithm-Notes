import sys
input = sys.stdin.readline

grade = []; score = []
for _ in range(20):
    cmd = list(input().split())
    grade.append(float(cmd[1])); score.append(cmd[2])
sm = 0; tg = 0
for g, s in zip(grade, score):
    if s == "A+":
        sm += 4.5 * g; tg += g
    if s == "A0":
        sm += 4.0 * g; tg += g
    if s == "B+":
        sm += 3.5 * g; tg += g
    if s == "B0":
        sm += 3.0 * g; tg += g
    if s == "C+":
        sm += 2.5 * g; tg += g
    if s == "C0":
        sm += 2.0 * g; tg += g
    if s == "D+":
        sm += 1.5 * g; tg += g
    if s == "D0":
        sm += 1.0 * g; tg += g
    if s == "F":
        sm += 0.0 * g; tg += g
    if s == "P":
        continue
print(sm/tg)