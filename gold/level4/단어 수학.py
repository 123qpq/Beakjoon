#1339
n = int(input())
dic = {}
for _ in range(n):
    temp = input()
    n = len(temp)
    for idx, t in enumerate(temp):
        dic[t] = dic.get(t, 0) + 10**(n-idx-1)
ans = 0
for i, v in enumerate(sorted(dic.values(), reverse=True)):
    ans += v*(9-i)
print(ans)