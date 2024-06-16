N = int(input())
_inputList = list(map(int, input().split()))

dp = [_inputList[0]]
answer = _inputList[0]

for idx in range(1, N):
    dp.append(max(dp[idx-1]+_inputList[idx],_inputList[idx]))
    answer = max(dp[idx],answer)

print(answer)
