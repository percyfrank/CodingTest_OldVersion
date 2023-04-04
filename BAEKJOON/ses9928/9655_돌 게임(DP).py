
dp = [0] * 1001

dp[1] = 1
dp[2] = 2
dp[3] = 1

for i in range(4,1001):
    dp[i] = min(dp[i-1],dp[i-3]) + 1

n = int(input())
if dp[n] % 2 == 0:
    print("CY")
else:
    print("SK")