#12015
import sys
import bisect
n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
res = [float('-inf')]
for s in sequence:
    if res[-1] < s:
        res.append(s)
    else:
        res[bisect.bisect_left(res, s)] = s
print(len(res)-1)