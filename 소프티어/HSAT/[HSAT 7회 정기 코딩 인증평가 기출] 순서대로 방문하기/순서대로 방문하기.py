import sys

N, M = map(int, input().split())

mapList = []
for _ in range(N):
    mapList.append(list(map(int, input().split())))

mustPoint = []
for _ in range(M):
    y,x = map(int, input().split())
    #y,x
    mustPoint.append((y-1,x-1 ))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
visit = [[0]*N for _ in range(N)]
path = []
def backTracking(temp):
    if temp[-1] == mustPoint[-1]:
        path.append(temp) 
        return
        
    y,x = temp[-1]
    #인접노드
    for idx in range(4):
        if (0<=y+dy[idx]<N) and (0<=x+dx[idx]<N):
            if visit[y+dy[idx]][x+dx[idx]] == 0:
                if mapList[y+dy[idx]][x+dx[idx]] == 0:
                    visit[y+dy[idx]][x+dx[idx]] = 1
                    backTracking(temp+[(y+dy[idx],x+dx[idx])])
                    visit[y+dy[idx]][x+dx[idx]] = 0

visit[mustPoint[0][0]][mustPoint[0][1]] = 1
backTracking([mustPoint[0]])

answer = 0
answerList = []
for line in path:
    try:
        idxs = []
        for x in mustPoint:
            idxs.append(line.index(x))
        if idxs == sorted(idxs):
            answer += 1 
            answerList.append(line)
    except:
        pass
print(answer)
#print(answerList)
