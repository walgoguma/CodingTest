from collections import deque

testCaseNum = int(input())

for _ in range(testCaseNum):
    # 0. 입력
    M, N, K = map(int, input().split())
    mapList = [[0]*M for i in range(N)]

    for x in range(K):
        x, y = map(int, input().split())
        mapList[y][x] = 1

    wormNum = 0

    visit = [[0] * M for _ in range(N)]
    # 상, 좌, 하, 우
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    for i in range (N):
        for j in range(M):
            if mapList[i][j] == 1:
                wormNum += 1

                # BFS
                queue = deque()
                queue.append((j, i))

                while queue:
                    #1. visit에 넣기
                    currentPosition = queue.popleft()
                    x = currentPosition[0]
                    y = currentPosition[1]

                    mapList[y][x] = 0
                    visit[y][x] = 1

                    #2. 인접 노드 추가하기
                    for idx in range(4):
                        if (0<=y+dy[idx]<N) and (0<=x+dx[idx]<M): #특정한 범위 내이면서
                            if mapList[y+dy[idx]][x+dx[idx]] == 1 : #배추가 존재하며
                                if (visit[y+dy[idx]][x+dx[idx]] == 0) and not((x,y) in queue): #방문하지 않거나 방문예정이 아닌 것
                                    queue.append((x+dx[idx], y+dy[idx]))


    print(wormNum)
