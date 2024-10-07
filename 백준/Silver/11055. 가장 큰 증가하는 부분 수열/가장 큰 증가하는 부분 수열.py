N = int(input())
sequence = list(map(int, input().split()))

dp = [0]*(N+1)
dp[1] = sequence[0]
answer = []
sumMax = dp[1]

for i,x in enumerate(sequence[1:], start=2):
    dp[i] = x
    for j in range(i):
        if x > sequence[j]:
            dp[i] = max(dp[i], dp[j+1]+x)

    sumMax = max(dp[i],sumMax)

print(sumMax)