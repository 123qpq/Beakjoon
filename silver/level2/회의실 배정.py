#1931
import sys
n = int(sys.stdin.readline())
meeting = []
for _ in range(n):
    s, e = map(int, sys.stdin.readline().split())
    meeting.append((e, s))
meeting.sort()
time = 0
res = 0
for  meet in meeting:
    if time <= meet[1]:
        time = meet[0]
        res += 1
print(res)