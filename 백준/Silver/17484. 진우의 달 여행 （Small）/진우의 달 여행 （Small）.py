# N: 세로, M: 가로
N, M = map(int, input().split())

space = []
for _ in range(N):
    space.append(list(map(int, input().split())))

dp = [[[6000]*3 for _ in range(M)] for _ in range(N)]
dp[0] = [[x]*3 for x in space[0] ]

for i in range(N-1):
    for j in range(M):
        #현재 dp에 있는 것이 다음 dp에 갈 수 있는 것
        for pos, x in enumerate(dp[i][j]):
            if pos == 2:
                if j+1 <M: dp[i+1][j+1][1] = min(dp[i+1][j+1][1], space[i+1][j+1]+x)
                dp[i+1][j][0] = min(dp[i+1][j][0],space[i+1][j]+x)
            elif pos == 0:
                if j+1 <M: dp[i+1][j+1][1] = min(dp[i+1][j+1][1], space[i+1][j+1]+x)
                if j-1 >=0: dp[i+1][j-1][2] = min(dp[i+1][j-1][2], space[i+1][j-1]+x)
            elif pos == 1:
                if j - 1 >= 0: dp[i + 1][j - 1][2] = min(dp[i + 1][j - 1][2], space[i + 1][j - 1] + x)
                dp[i+1][j][0] = min(dp[i+1][j][0],space[i+1][j]+x)

answer = 6000
for line in dp[-1]:
    for x in line:
        answer= min(answer,x)
print(answer)