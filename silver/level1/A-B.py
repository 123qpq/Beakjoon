#16953
import sys
from collections import deque
a, b = map(int, sys.stdin.readline().split())
q = deque([a])
cnt = 0
while q:
    cnt += 1
    for _ in range(len(q)):
        now = q.popleft()
        if now == b:
            print(cnt)
            exit(0)
        else:
            mul = now * 2
            pls = now * 10 + 1
            if mul <= b:
                q.append(mul)
            if pls <= b:
                q.append(pls)
print(-1)