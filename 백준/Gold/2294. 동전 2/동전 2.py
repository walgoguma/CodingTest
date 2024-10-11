N,K = map(int, input().split())
coins =[]
for _ in range(N):
    coins.append(int(input()))

dp = [100000]*(K+1)
dp[0]=0
for x in coins:
    for i in range(x,K+1):
        dp[i] = min(dp[i-x]+1,dp[i])

if dp[K] == 100000:
    print(-1)
else:
    print(dp[K])