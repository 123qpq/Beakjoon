n = int(input())
wines = [0] + [int(input()) for _ in range(n)]
dp = [0, wines[1]] # 앞에꺼를 마셨을 때 / 앞앞꺼를 마셨을 때
if n > 1:
    dp.append(wines[1]+wines[2])
for i in range(3, n+1):
    dp.append(max(dp[i-1], dp[i-2] + wines[i], dp[i-3] + wines[i-1] + wines[i]))

print(dp[-1])