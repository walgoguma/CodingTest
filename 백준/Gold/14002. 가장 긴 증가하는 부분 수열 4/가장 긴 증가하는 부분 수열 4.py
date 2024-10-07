N = int(input())
sequence = list(map(int, input().split()))

dp = [[0]for _ in range(N+1)]
dp[1] = [sequence[0]]
answer = [sequence[0]]
# 5 3 8 8 2 4 8 2 3 4
for i,x in enumerate(sequence[1:], start=2):
    dp[i] = [x]
    for j in range(i):
        if x > sequence[j]:
            if len(dp[i])<len(dp[j+1]+[x]):
                dp[i] = dp[j+1]+[x]
    if len(dp[i]) > len(answer):
        answer = dp[i]

print(len(answer))
print(*answer)