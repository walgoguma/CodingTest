from sys import stdin

#0. 입력 N:정점 개수, M:간선개수
N,M = map(int, input().split())

node = {}
for x in range(M):
    node1, node2 = map(int,  stdin.readline().split())
    if node.get(node1):
        node[node1].append(node2)
    else:
        node[node1] = [node2]

    if node.get(node2):
        node[node2].append(node1)
    else:
        node[node2] = [node1]


#1. DFS
visit = [0]*(N+1)
stack = []
start = 1
cnt = 0

for y in range(1,N+1):
    if visit[y] == 0:
        stack.append(y)
        visit[y] = 1

        #탐색 시작
        while stack:
            now = stack.pop()

            #인접노드 선택
            if node.get(now):
                for x in node[now]:
                    if visit[x]==0:
                        stack.append(x)
                        visit[x]=1
        cnt += 1

print(cnt)