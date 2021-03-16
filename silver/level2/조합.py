#2407
import sys
n, m = map(int, sys.stdin.readline().split())
res = 1
if n // 2 < m:
    m = n - m
for x in range(n-m+1, n+1):
    res *= x
for y in range(1, m+1):
    res //= y
print(res)