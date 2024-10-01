from collections import deque
import copy

from collections import deque


# N: 세로, M: 가로
N = int(input())
space = []
current = 0 #(y,x)
find = False
for idx in range(N):
    space.append(list( map(int, input().split())))

    if find == False:
        for i, x in enumerate(space[-1]):
            if x == 9:
                current = (idx,i)
                space[idx][i] = 0
                find = True

dx = [0,-1,1,0]
dy = [-1,0,0,1]
visit = [[0]*N for _ in range(N)]

size = 2
answer = 0
eat = 0
while True:

    #1. 완전 탐색: 물고기 위치 + 거리
    fish = []
    queue = deque()
    queue.append((0,current[0],current[1]))
    visits = [[0] * N for _ in range(N)]
    current = 0
    distances = {}

    while queue:
        distance, y, x = queue.popleft()
        if space[y][x] != 0 and space[y][x]<size:
            if distances.get(distance,-1) != -1:
                distances[distance].append((y,x))
            else:
                distances[distance] = [(y,x)]

        for idx in range(4):
            if 0<=y+dy[idx]<N and 0<=x+dx[idx]<N:
                if visits[y+dy[idx]][x+dx[idx]] == 0:
                    if space[y+dy[idx]][x+dx[idx]] <= size:
                        queue.append((distance+1, y+dy[idx], x+dx[idx]))
                        visits[y+dy[idx]][x+dx[idx]] = 1

    # print(distances)
    for d in distances.items():
        temp = sorted(d[1])
        # print(temp)
        y,x = temp[0]
        space[y][x] = 0
        current = (y,x)
        answer += d[0]
        eat += 1
        if size == eat:
            size += 1
            eat = 0
        break

    if current == 0:
        break

    # for x in space:
    #     print(x)
    # print("answer:{} , size:{}".format(answer, size))
    # print("")
print(answer)