import copy

# 방향 -  ↑(1), ↖(2), ←(3), ↙(4), ↓(5), ↘(6), →(7), ↗(8)
dx = [100, 0,  -1, -1, -1, 0, 1, 1,  1]
dy = [100, -1, -1,  0,  1, 1, 1, 0, -1]

def fishMove(fishMap,eat):
    stop = True
    for find in range(1,17):
        y, x = -1, -1
        direction = -1
        if  find not in eat:
            for i in range(4):
                for j in range(4):
                    if fishMap[i][j][0] == find:
                        y,x = i, j
                        direction = fishMap[i][j][1]
                        break

            switch = False
            for _ in range(8):
                if (0<=y+dy[direction]<4) and (0<=x+dx[direction]<4): # 범위를 벗어나지 않는 선에서
                   if fishMap[y+dy[direction]][x+dx[direction]][0] != -1: # 상어를 만나지 않는다면
                       fishMap[y][x],fishMap[y + dy[direction]][x + dx[direction]] = fishMap[y + dy[direction]][x + dx[direction]],fishMap[y][x] # 빈칸일 경우 빈칸이 아닐 경우
                       if fishMap[y + dy[direction]][x + dx[direction]][0] != 0:
                           fishMap[y + dy[direction]][x + dx[direction]][1] = direction
                       switch = True
                       stop = False
                       break

                if switch == False:
                    direction = (direction%8)+1
    if stop == True:
        return stop
    else:
        return fishMap

#1. 입력
fishes = []

for i in range(4):
    temp = list(map(int,input().split()))
    fishes.append([])
    for j in range(0,8,2):

        fishes[i].append(temp[j:j+2])

answer = 0
def backTracking(fishMap,eat, eatAmount):
    global answer
    # 물고기 이동하기
    fishMoveResult = fishMove(fishMap,eat)

    #더이상 물고기가 없으면 종료
    if fishMoveResult == True:
        answer = max(eatAmount, answer)
        return
    else:
        #상어 위치 찾기
        y,x = -1, -1
        direction = -1
        for i in range(4):
            for j in range(4):
                if fishMoveResult[i][j][0] == -1:
                    y, x = i, j
                    direction = fishMoveResult[i][j][1]
                    break

        #상어가 먹을 수 있는 경우마다 backTracking
        move =False
        for i in range(1,4):
            temp = copy.deepcopy(fishMoveResult)
            if (0 <= y + dy[direction]*i < 4) and (0 <= x + dx[direction]*i < 4):
                if temp[y + dy[direction]*i][x + dx[direction]*i][0] != 0 and temp[y + dy[direction]*i][x + dx[direction]*i][0] != -1:
                    move = True

                    saveEat = temp[y + dy[direction]*i][x + dx[direction]*i][0]
                    saveDirection = temp[y + dy[direction]*i][x + dx[direction]*i][1]
                    saveSharkPosition = temp[y][x]

                    eat.append(saveEat)
                    eatAmount+=saveEat
                    temp[y][x] = [0,0]
                    temp[y + dy[direction]*i][x + dx[direction]*i][0] = -1
                    backTracking(temp, eat, eatAmount)

                    eat.remove(saveEat)
                    eatAmount -= saveEat

        if move == False:
            answer = max(eatAmount, answer)
            return



# 상어위치 초기화: -1
startEat = fishes[0][0][0]
fishes[0][0] = [-1,fishes[0][0][1]]
backTracking(fishes,[startEat], startEat)

print(answer)
