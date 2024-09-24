
# N: 세로, M: 가로
N,M = map(int, input().split())

#d == 0인 경우 북쪽, 1인 경우 동쪽, 2인 경우 남쪽, 3인 경우 서쪽
#start x,start y
sy,sx,d = map(int, input().split())
current = (sy,sx)

room = []
for _ in range(N):
    room.append(list(map(int, input().split())))

direction = [(-1, 0), (0,1), (1,0), (0,-1)]
rear = [(1, 0), (0,-1), (-1,0), (0,1)]
fornt = [(-1, 0), (0,1), (1,0), (0,-1)]

#1.
answer = 0
while True:
    if room[current[0]][current[1]] == 0:
        room[current[0]][current[1]] = -1
        answer += 1

    #청소되지 않은 칸 찾기
    cnt = 0
    for i in range(4):
        if room[current[0] + direction[i][0]][current[1] + direction[i][1]] == 1\
                or room[current[0] + direction[i][0]][current[1] + direction[i][1]] == -1:
            cnt += 1

    if cnt == 4: #청소되지 않은 빈칸이 없는 경우
        if 0<=current[0]+rear[d][0]<N and 0<=current[1]+rear[d][1]<M:
            if room[current[0]+rear[d][0]][current[1]+rear[d][1]] != 1:
                current = (current[0]+rear[d][0], current[1]+rear[d][1])
            else:
                break
        else:
            break

    else: #청소되지 있는 빈칸이 없는 경우
        #반시계 방향으로 회전
        for _ in range(4):
            d = (d + 3) % 4
            if room[current[0] + fornt[d][0]][current[1] + fornt[d][1]] == 0:
                current = (current[0] + fornt[d][0], current[1] + fornt[d][1])
                break

print(answer)