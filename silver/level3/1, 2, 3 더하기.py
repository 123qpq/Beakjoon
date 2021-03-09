#9095
n = int(input())
lst = [int(input()) for _ in range(n)]
maxx = max(lst) + 1
dp = [0, 1, 2, 4] + [0] * (maxx-4)

for i in range(4, maxx):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
for i in lst:
    print(dp[i])