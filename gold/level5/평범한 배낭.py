#12865
import sys
n, maxx = map(int, sys.stdin.readline().split())
lst = []
dp = [0] * (maxx+1)
for _ in range(n):
    kilo, value = map(int, sys.stdin.readline().split())
    for i in range(maxx, kilo-1, -1):
        dp[i] = max(dp[i], dp[i-kilo] + value)
print(dp[-1])