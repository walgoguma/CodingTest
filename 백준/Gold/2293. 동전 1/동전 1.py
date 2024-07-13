import sys

n, k = map(int, input().split())

_coin=[]
for _ in range(n):
    _coin.append(int(input()))
_coin = sorted(_coin)

dp=[0 for _ in range(k+1)]
dp[0]=1

# 첫번째 줄
for i in range(1,k+1):
    #만약 나누어 떨아지면 0
    if i%_coin[0]==0:
        dp[i]=1
    else:
        dp[i] = 0

#나머지 줄
for i in range(1,n):
    if _coin[i] <= k:
        for j in range(_coin[i], k + 1):
            dp[j] = dp[j] + dp[j-_coin[i]]

print(dp[k])