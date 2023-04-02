

n = int(input())
dp = [0] * (1000001)
pre = [0] * (1000001)

dp[1] = 0
pre[1] = 0

for i in range(2,n+1):
    dp[i] = dp[i-1] + 1
    pre[i] = i-1
    if i % 2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = min(dp[i], dp[i//2] + 1)
        pre[i] = i // 2
    if i % 3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = min(dp[i], dp[i//3] + 1)
        pre[i] = i // 3

print(dp[n])
tmp = n
while tmp >= 1:
    print(tmp, end = ' ')
    tmp = pre[tmp]

