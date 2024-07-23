import sys
from collections import deque

#0. 입력
node, edge, start = map(int, input().split())

graph = {}
for _ in range(edge):
    node1, node2 = map(int, input().split())

    if graph.get(node1):
        graph[node1].append(node2)
    else:
        graph[node1] = [node2]

    if graph.get(node2):
        graph[node2].append(node1)
    else:
        graph[node2] = [node1]

for key,value in graph.items():
    graph[key] = list(set(value))

#DFS
visit = []
stack = []
stack.append(start)

while stack: #파이썬은 [],False, None을 동일시 여긴다.
    #1. visit에 넣기
    if (stack[-1] not in visit):
        visit.append(stack.pop())
    else:
        stack.pop()

    #2. 인접 노드 표시하기
    if graph.get(visit[-1]):
        nearNode = graph[visit[-1]]
    else:
        break
    #2-1. 가장 값이 작은 친구를 가장 마지막에 넣어주기 위한 선언
    nearNode = sorted(nearNode,reverse=True)
    for x in nearNode:
        if (x not in visit):
            stack.append(x)


print(*visit)

#BFS
visit = []
queue = deque()
queue.append(start)

while queue:
    #1. visit에 넣기
    visit.append(queue.popleft())

    #2. 인접 노드 표시하기
    if graph.get(visit[-1]):
        nearNode = graph[visit[-1]]
    else:
        break

    nearNode = sorted(nearNode)
    for idx, x in enumerate(nearNode):
        if not(x in visit) and not(x in queue):
                queue.append(x)

print(*visit)