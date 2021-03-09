n, r, c = map(int, input().split())

nn = 2**n
lt = 0
rt = nn*nn-1
for i in range(n, 0, -1):
    mid = (lt + rt) // 2
    if r < 2**i / 2:
        rt = mid
    else:
        lt = mid
    mid = (lt + rt) // 2
    if c < 2**i / 2:
        rt = mid
    else:
        lt = mid
if c % 2 == 0:
    print(lt)
else:
    print(rt)