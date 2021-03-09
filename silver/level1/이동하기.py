#11048
import sys
y, x = map(int, input().split())
before = list(map(int, sys.stdin.readline().split()))
for i in range(1, x):
    before[i] += before[i-1]
if y == 1:
    print(before[-1])
    sys.exit(0)
for _ in range(y-1):
    now = list(map(int, sys.stdin.readline().split()))
    now[0] += before[0]
    for i in range(1, x):
        now[i] += max(now[i-1], before[i])
    before = now
print(now[-1])