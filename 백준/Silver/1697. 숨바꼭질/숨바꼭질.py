from collections import deque

#0. 입력 N:현재 술래 위치, K:숨어 있는 위치
N,K = map(int, input().split())

#1. BFS
visit = [0]*100001
queue = deque()
queue.append((N,1)) #(이동할 위치, flag: flag가 1이면 1초가 더 지났을 경우의 레벨을 검사하겠다는 의미)
second = 0

while queue:
    #방문할 노드
    position,flag = queue.popleft()
    visit[position] = 1

    #만약 술래를 찾았다면 종료
    if position == K:
        break

    #인접 노드
    dx = [-1, 1, position]
    for idx,move in enumerate(dx):
        if (0<= position+move <=100000):
            if visit[position+move] !=1:
                queue.append((position+move,0))
                visit[position + move] = 1

    #만약 플래그가 존재한다면, 다음번부터는 1초가 더 지났을 경우를 탐색하겠다는 의미
    if flag == 1:
        temp1,temp2 = queue.pop()
        queue.append((temp1,1))
        second+=1

print(second)