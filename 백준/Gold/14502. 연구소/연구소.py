import copy
from collections import deque

# N: 세로, M: 가로
N,M = map(int, input().split())

container = []
wallCnt = 0
for _ in range(N):
    container.append(list(map(int, input().split())))
    wallCnt += container[-1].count(1)
wallCnt += 3

answer = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def dfs(wall):
    global answer
    queue = deque()
    visit = [[0]*M for _ in range(N)]
    containerCopy = copy.deepcopy(container)
    virusCnt = 0

    for y,x in wall:
        containerCopy[y][x] = 1

    for i in range(N):
        for j in range(M):
            if containerCopy[i][j] == 2 and visit[i][j] == 0:
                queue.append((i,j))
                visit[i][j] = 1

        while queue:
            y,x = queue.popleft()
            containerCopy[y][x] = 2
            virusCnt += 1

            for idx in range(4):
                if 0<= y+dy[idx]< N and 0<= x+dx[idx]< M :
                    if containerCopy[y+dy[idx]][x+dx[idx]] != 1:
                        if visit[y+dy[idx]][x+dx[idx]] == 0:
                            queue.append((y+dy[idx], x+dx[idx]))
                            visit[y + dy[idx]][x + dx[idx]] = 1

    answer = max(answer,N*M - wallCnt - virusCnt)


visitBack = [[0]*M for _ in range(N)]
cnt = 1
def backTraking(temp):
    global cnt
    if len(temp) == 3:
        dfs(temp)
        return
    for i in range(N):
        for j in range(M):
            if container[i][j] == 0:
                if visitBack[i][j] == 0:
                    visitBack[i][j] = 1
                    backTraking(temp+[(i,j)])
                    visitBack[i][j] = 0

backTraking([])
print(answer)