days = int(input())
dp = [0]*(days+2)
maxPay = 0


for day in range(1, days+1):
    period, pay = map(int, input().split())
    dp[day] = max(dp[day], dp[day-1])
    if day + period <= days+1:
        dp[day + period] = max(dp[day + period], dp[day]+pay)
        maxPay = max(maxPay, dp[day + period])

print(maxPay)