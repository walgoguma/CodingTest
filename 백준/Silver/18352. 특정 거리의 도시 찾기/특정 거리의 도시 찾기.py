from collections import deque

#N:도시의 개수, M:도로의 개수, K:거리 정보, X: 출발도시의 번호
N, M, K, X = map(int,input().split())
path = [[]for _ in range(N+1)]

for _ in range(M):
    start, end = map(int,input().split())
    path[start].append(end)

answer = []

queue = deque()
visit = [0] * (N+1)

queue.append((0,X))
visit[X] = 1

while queue:
    distance, node = queue.popleft()

    if distance == K:
        answer.append(node)

    for x in path[node]:
        if visit[x] == 0:
            queue.append((distance+1, x))
            visit[x] = 1

if len(answer) == 0:
    print(-1)
else:
    for x in sorted(answer):
        print(x)