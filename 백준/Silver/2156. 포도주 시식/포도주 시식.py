#0. 입력 N:정점 개수, M:간선개수
N = int(input())

grape = []
for _ in range(N):
        grape.append(int(input()))

dp = [0,0]
flag = 0

for i in range(N):
    if flag == 0:
        dp.append(dp[i+1] + grape[i])
        flag = 1
    elif flag == 1:
        dp.append(dp[i + 1] + grape[i])
        flag = 2
    elif flag == 3:
        dp.append(dp[i + 1] + grape[i])
        flag = 2
    elif flag ==2:
        temp = [dp[i] + grape[i], dp[i-1]+grape[i-1]+grape[i], dp[i+1]]
        dp.append(max(temp))
        flag = temp.index(dp[i+2])+1

print(dp[-1])