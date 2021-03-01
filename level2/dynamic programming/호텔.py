#1106
want, n = map(int, input().split())
dp = [0] + [float('inf')] * (want+1)
lst = []
plus = 0
for _ in range(n):
    cost, client = map(int, input().split())
    lst.append((cost, client))
    plus = max(plus, client)

dp += [float('inf')] * plus

for l in lst:
    for i in range(l[1], len(dp)):
        dp[i] = min(dp[i], dp[i - l[1]] + l[0])
print(min(dp[want:]))