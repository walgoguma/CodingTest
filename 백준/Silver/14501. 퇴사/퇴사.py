N = int(input())
_meeingList = []
for _ in range(N):
    _meeingList.append(list(map(int, input().split())))

dp = [0]*(N+1) #현날짜까지 받을 수 있는 최대 금액
answer = 0

for i, x in enumerate(_meeingList):
    prevMax = 0
    if (x[0]+i<=N):
        if i !=0:
            prevMax = max(dp[0 if i-5<0 else i-5 : i])
        dp[x[0]+i] = max(dp[x[0]+i],dp[i]+x[1], prevMax+x[1])
        answer = max(answer,dp[x[0]+i])

print(answer)