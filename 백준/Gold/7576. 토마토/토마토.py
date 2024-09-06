import sys
import copy

N, M = map(int, input().split())

#현재 상자의 토마토
box = []
for _ in range(M):
    box.append(list(map(int, input().split())))
#현재 토마토가 존재해 탐색을 시작해야할 곳
searchList = []
for y, line in enumerate(box):
    for x in filter( lambda idx: line[idx]==1  , range(len(line))):
        searchList.append((y,x))
#탐색을 한 곳
visit = [[0]*N for _ in range(M)]
#DFS관련 필요 내용 정의
stack = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

answer = -1
#DFS 시작
while searchList:
    newserchList = []
    for posision in searchList:
        if visit[posision[0]][posision[1]] == 0 :
            stack.append(posision)
            visit[posision[0]][posision[1]] = 1

        while stack:
            y, x = stack.pop()
            for idx in range(4):
                if (0 <= y + dy[idx] < M) and (0 <= x + dx[idx] < N):
                    if visit[y + dy[idx]][x + dx[idx]] == 0:
                        if box[y + dy[idx]][x + dx[idx]] == 1:
                            stack.append((y + dy[idx], x + dx[idx]))
                            visit[y + dy[idx]][x + dx[idx]] = 1
                        elif box[y + dy[idx]][x + dx[idx]] == 0:
                            newserchList.append((y + dy[idx], x + dx[idx]))

    answer+=1
    searchList = newserchList
    for y,x in searchList:
        box[y][x] = 1

cnt = 0
for i in range(M):
    for j in range(N):
        if box[i][j] == 0:
            print(-1)
            sys.exit()
print(answer)

