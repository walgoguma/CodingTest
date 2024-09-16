w,h = map(int, input().split())
house = [[0]*(w+2)]
for _ in range(h):
    house.append([0]+list(map(int, input().split()))+[0])
house.append([0] * (w + 2))

stack = []
visit = [[0]*(w+2) for _ in range(h+2)]

dxOdd = [-1,  0,0,  1,1,1]
dyOdd = [ 0, -1,1, -1,0,1]
dxEven = [-1,-1,-1,  0,0, 1]
dyEven = [-1, 0, 1, -1,1, 0]

answer = 0

stack.append((0, 0))
visit[0][0] = 1

while stack:
    y,x = stack.pop()
    if y%2==0:
        dx = dxEven
        dy = dyEven
    else:
        dx = dxOdd
        dy = dyOdd

    findCnt = 0
    for idx in range(6):
        if (0<=y+dy[idx]<h+2) and (0<=x+dx[idx]<w+2):
            if visit[y + dy[idx]][x + dx[idx]] == 0:
                if house[y+dy[idx]][x+dx[idx]] == 0:
                        stack.append((y+dy[idx],x+dx[idx]))
                        visit[y+dy[idx]][x+dx[idx]] = 1
                else:
                    answer +=1

print(answer)