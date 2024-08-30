from collections import deque

def solution(board):
    answer = 0
    distance = 0

    
    N = len(board[0])
    M = len(board)
    start = (0,0,distance)
    goal = (0,0)
    
    findStart = False
    findGoal = False
    escape = False
    
    for j, element in enumerate(board):
        for i, x in enumerate(element):
            if findStart and findGoal:
                break
                
            if x == 'R':
                start = (j,i,distance)
                findStart = True
            elif x =='G':
                goal = (j,i)
                findGoal = True

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    visit = [[0]*N for _ in range(M)]
    queue = deque()    
    queue.append(start)
    visit[start[0]][start[1]] = 1
    
    
    while queue:
        #현재 탐색할 위치
        pointY,pointX, distance = queue.popleft()
        #distance += 1
        
        if  board[pointY][pointX] == 'G':
            answer = distance 
            escape =True
    
        #인접 노트 찾기
        for idx in range(4):
            #만약 한 칸 갈수 있다면?
            if (0<= pointY+ dy[idx] <M) and (0<= pointX+dx[idx] <N): 
                if board[pointY+ dy[idx]][pointX+dx[idx]] != 'D':
                    #슬라이딩을 통해 도착하는 위치 찾기
                    cnt = 1 
                    while True:
                        if (((0<= pointY+ dy[idx]*(cnt+1) <M) and (0<= pointX+dx[idx]*(cnt+1)<N)) and \
                            (board[pointY+ dy[idx]*(cnt+1)][pointX+dx[idx]*(cnt+1)] != 'D')):
                            cnt +=1
                        else:
                            break
                           
                    if  visit[pointY+ dy[idx]*(cnt)][pointX+dx[idx]*(cnt)] == 0:
                        queue.append((pointY+ dy[idx]*(cnt), pointX+dx[idx]*(cnt), distance+1))
                        visit[pointY+ dy[idx]*(cnt)][pointX+dx[idx]*(cnt)] = distance+cnt                            
        # for line in visit:
        #     print(line)
        # print("")
                    


    if escape == True:
        return answer
    else:
        return -1
