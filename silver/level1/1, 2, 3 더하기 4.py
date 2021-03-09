#15989
import sys
n = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(n)]
end = max(lst) + 1
dp = [0] * end
dp[0] = 1
for i in range(1, 4):
    for j in range(i, end):
        dp[j] += dp[j-i]
    print(dp)
for num in lst:
    print(dp[num])