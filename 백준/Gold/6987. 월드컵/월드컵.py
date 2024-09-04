import copy

scores = []

for _ in range(4):
    temp = list(map(int, input().split()))
    score = []
    for i in range(6):
        score.append(temp[3*i:3*i+3])
    scores.append(score)
visit = [0]*6

candidate = []
def backtracking(idx,temp):
    global candidate
    if len(temp) ==2:
        plus = []
        for i, case in enumerate(candidate):
            if(case[temp[0]][0]>0 and case[temp[1]][2]>0):
                temp1 = copy.deepcopy(case)
                temp1[temp[0]][0] -=1
                temp1[temp[1]][2] -=1
                plus.append(temp1)
            if(case[temp[0]][1]>0 and case[temp[1]][1]>0):
                temp1 = copy.deepcopy(case)
                temp1[temp[0]][1] -=1
                temp1[temp[1]][1] -=1
                plus.append(temp1)
            if(case[temp[0]][2]>0 and case[temp[1]][0]>0):
                temp1 = copy.deepcopy(case)
                temp1[temp[0]][2] -=1
                temp1[temp[1]][0] -=1
                plus.append(temp1)

        candidate = plus
        return

    for i in range(6):
        if len(temp)==0 or temp[-1] < i:
            if visit[i] == 0:
                visit[i] = 1
                backtracking(idx, temp +[i])
                visit[i] = 0

answer = []
for idx, score in enumerate(scores):
    candidate.append(score)
    backtracking(idx, [])

    ok = False
    for line in candidate:
        if line == [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]:
            answer.append(1)
            ok = True
            break

    if ok == False:
        answer.append(0)

    candidate = []
print(*answer)