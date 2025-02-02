from collections import deque

N = int(input())
M = int(input())
graph = [[]for _ in range(N+1)]
for _ in range(M):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

#BFS
queue = deque()
visit = [[0] for _ in range(N+1)]

queue.append(1)
visit[1] = 1
virusCnt = 0

#상, 좌, 하, 우
dx = [0,1,0,-1]
dy = [-1,0,1,0]

while queue:
    #1. 방문할 노드 확인
    current = queue.popleft()

    #2.인접노드 추기
    for x in graph[current]:
        if visit[x] != 1:
            queue.append(x)
            visit[x] = 1
            virusCnt += 1

print(virusCnt)