import sys
n = int(sys.stdin.readline())
nums = list(sys.stdin.readline().split())
dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = 1
    if i < n-1 and nums[i] == nums[i+1]:
        check = 0
        while nums[i-check] == nums[i+1+check]:
            dp[i-check][i+1+check] = 1
            check += 1
            if i-check < 0 or n-1 < i+1+check:
                break
    if i < n-2 and nums[i] == nums[i+2]:
        check = 0
        while nums[i-check] == nums[i+2+check]:
            dp[i-check][i+2+check] = 1
            check += 1
            if i-check < 0 or n-1 < i+2+check:
                break

q = int(sys.stdin.readline())
for _ in range(q):
    s, e = map(int, sys.stdin.readline().split())
    print(dp[s-1][e-1])