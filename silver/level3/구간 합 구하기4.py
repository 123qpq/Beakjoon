#11659
import sys
n, m = map(int, sys.stdin.readline().split())
numlist = map(int, sys.stdin.readline().split())
summ = [0]
for i in numlist:
    summ.append(summ[-1] + i)
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(summ[e] - summ[s-1])