#1697
import sys
from collections import deque

me, you = map(int, input().split())
if you < me:
    print(me-you)
    sys.exit(0)
#13549
q = deque()
q.append((me, 0))
visited = [float('inf')] * 100001
res = float('inf')
while q:
    for _ in range(len(q)):
        temp = q.popleft()
        now = temp[0]
        cnt = temp[1]
        if now == you:
            res = cnt
        elif cnt < res:
            if now+1 <= 100000 and cnt < visited[now+1]:
                visited[now+1] = cnt+1
                q.append((now+1, cnt+1))
            if 0 <= now-1 and cnt < visited[now-1]:
                visited[now-1] = cnt+1
                q.append((now-1, cnt+1))
            if now < you and now*2 <= 100000 and cnt < visited[now*2]:
                visited[now*2] = cnt
                q.append((now*2, cnt))
print(res)