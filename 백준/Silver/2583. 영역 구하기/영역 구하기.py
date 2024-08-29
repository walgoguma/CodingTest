#0. 입력 M:세로, N:가로, K: 직사각형 개수
M,N,K = map(int,input().split())

maplist = [[1]*N for _ in range(M)]
for _ in range(K):
    x1,y1,x2,y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(M-y2, M-y1):
            maplist[j][i] = 0

#DFS
stack = []
visit = [[0]*N for _ in range(M)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

areaCnt = 0
areaSize=[]

for i in range(N):
    for j in range(M):
        if maplist[j][i] == 1 and visit[j][i] == 0:
            stack.append((j,i))
            visit[j][i] = 1
            areaSize.append(0)

            while stack:
                y,x = stack.pop()
                areaSize[areaCnt] += 1

                for idx in range(4):
                    if (0<=y+dy[idx]<M) and (0<=x+dx[idx]<N):
                        if maplist[y+dy[idx]][x+dx[idx]] == 1 and visit[y+dy[idx]][x+dx[idx]] ==0:
                            stack.append((y+dy[idx],x+dx[idx]))
                            visit[y+dy[idx]][x+dx[idx]] = 1

            areaCnt += 1

print(areaCnt)
areaSize = sorted(areaSize)
print(*areaSize)
