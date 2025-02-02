N = int(input())
stair = [0,0,0]
for _ in range(N):
    stair.append(int(input()))

dp = [0]*(N+3)
for i in range(3,N+3):
    dp[i] = max(dp[i-2]+stair[i], dp[i-3]+stair[i-1]+stair[i])

print(dp[-1])
