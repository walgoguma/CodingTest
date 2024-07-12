import sys

#0. 입력
N = int(input())
if N == 1:
    print(0)
    sys.exit()

jumps = []
for _ in range(N-1):
    jumps.append(list(map(int, input().split())))
k = int(input())

if N == 2:
    print(jumps[0][0])
    sys.exit()

dp = [0]*N
for i, jump in enumerate(jumps):
    if i+1 < N:
        if dp[i+1] != 0:
            dp[i+1] = min(dp[i+1],dp[i]+jump[0])
        else:
            dp [i+1] = dp[i]+jump[0]

    if i+2 < N:
        if dp[i+2] != 0:
            dp[i+2] = min(dp[i+2],dp[i]+jump[1])
        else:
            dp [i+2] = dp[i]+jump[1]
    #print(dp)


minE= dp[-1]

if N >= 3:
    for i in range(N-3):
        dp1 = dp.copy()
        dp1[i + 3] = min(dp[i + 3], dp[i] + k)

        for j in range(i,N):
            if j + 1 < N:
                if dp1[j + 1] != 0:
                    dp1[j + 1] = min(dp1[j + 1], dp1[j] + jumps[j][0])
                else:
                    dp1[j + 1] = dp1[j] + jumps[j][0]

            if j + 2 < N:
                if dp1[j + 2] != 0:
                    dp1[j + 2] = min(dp1[j + 2], dp1[j] + jumps[j][1])
                else:
                    dp1[j + 2] = dp1[j] + jumps[j][1]

        minE = min (minE, dp1[N-1])

    print(minE)