#0. 입력 N:정점 개수, M:간선개수
N = int(input())

mapList = []
for _ in range(N):
    temp = []
    for x in input():
        temp.append(int(x))

    mapList.append(temp)

#1.
areaCnt = 0
houseCnt = []

visit = [[0]*N for _ in range(N)]
stack = []
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for seq in range(N*N):
    y = seq // N
    x = seq % N

    if mapList[y][x] == 1 and visit[y][x] == 0:
        stack.append((y,x))
        visit[y][x] = 1
        houseCnt.append(0)

        #DFS 실행
        while stack:
            nowY,nowX = stack.pop()
            houseCnt[areaCnt] += 1

            #인접노드 추가
            for idx in range(4):
                if (0<=nowY+dy[idx]<N) and (0<=nowX+dx[idx]<N):
                    if visit[nowY+dy[idx]][nowX+dx[idx]] == 0 and mapList[nowY+dy[idx]][nowX+dx[idx]] == 1:
                        stack.append((nowY+dy[idx], nowX+dx[idx]))
                        visit[nowY + dy[idx]][nowX + dx[idx]] = 1

        areaCnt +=1

print(areaCnt)
houseCnt = sorted(houseCnt)
for x in houseCnt:
    print(x)