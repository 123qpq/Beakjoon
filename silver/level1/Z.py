#1074
n, r, c = map(int, input().split())
res = 0
for i in range(n, 1, -1):
    mid = 2**(i-1)
    if mid <= r and mid <= c: #4사분면
        res += mid*mid*3
        r -= mid
        c -= mid
    elif mid <= r and c < mid: #3사분면
        res += mid*mid*2
        r -= mid
    elif r < mid and mid <= c: #2사분면
        res += mid*mid
        c -= mid

if r == 0 and c == 0:
    print(res)
elif r == 1 and c == 0:
    print(res+2)
elif r == 0 and c == 1:
    print(res+1)
else:
    print(res+3)