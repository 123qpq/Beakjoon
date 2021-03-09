#1806
n, m = map(int, input().split())
lst = list(map(int, input().split()))
start, total = 0, 0
cnt = 0
res = float('inf')
for num in lst:
    total += num
    cnt += 1
    while m <= total-lst[start]:
        total -= lst[start]
        start += 1
        cnt -= 1
    if m <= total:
        res = min(cnt, res)

if res == float('inf'):
    print(0)
else:
    print(res)