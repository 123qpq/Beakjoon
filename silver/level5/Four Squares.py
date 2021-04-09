#17626
n = int(input())
dp = [0, 1, 2]
for i in range(3, n+1):
    res = 3
    pv = 1
    while pv**2 <= i:
        res =min(res, dp[i-(pv**2)])
        pv += 1
    dp.append(res+1)
print(dp[n])