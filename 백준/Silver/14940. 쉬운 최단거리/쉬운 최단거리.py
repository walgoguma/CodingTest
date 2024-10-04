from collections import deque


#N: 세로, K: 가로
N,M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

answer = [[0]*M for _ in range(N)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

start = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            start = (i,j)
            break

queue = deque()
visit = [[0]*M for _ in range(N)]
visit[start[0]][start[1]] = 1

queue.append((0,start[0],start[1]))

while queue:
    distance, y, x = queue.popleft()

    answer[y][x] = distance

    for idx in range(4):
        if 0<=y+dy[idx]<N and 0<=x+dx[idx]<M:
            if graph[y+dy[idx]][x+dx[idx]] != 0:
                if visit[y+dy[idx]][x+dx[idx]] == 0:
                    queue.append((distance+1,y+dy[idx],x+dx[idx]))
                    visit[y+dy[idx]][x+dx[idx]] = 1
            else:
                visit[y + dy[idx]][x + dx[idx]] = -1

for i in range(N):
    for j in range(M):
        if visit[i][j] == 0 and graph[i][j] != 0:
            answer[i][j] = -1
        elif visit[i][j] == 0 and graph[i][j] == 0:
            answer[i][j] = 0
for a in answer:
    print(*a)