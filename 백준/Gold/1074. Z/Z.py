N, r, c = map(int, input().split())

start = (0,0)
length = 2**N
direction = [(0,0), (1,0),(0,1),(1,1)]

answer = 0
for _ in range(N): #4등분을 N번 할 것임
    for i in range(4):
        if (start[0]+direction[i][0]*(length//2) <= c <= start[0]+(direction[i][0]+1)*(length//2)-1 and
            start[1] + direction[i][1]*(length // 2) <= r <= start[1] + (direction[i][1]+1)*(length // 2)-1):
            start = (start[0]+direction[i][0]*(length//2), start[1] + direction[i][1]*(length // 2))
            break
        else:
            answer += (length//2)**2

    length = length //2
print(answer)