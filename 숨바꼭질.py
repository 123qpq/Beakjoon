#1697
import sys
from collections import deque

me, you = map(int, input().split())
if you < me:
    print(me-you)
    sys.exit(0)
#1697
q = deque([me])
visited = [False] * 100001
cnt = 0
while q:
    cnt += 1

    for _ in range(len(q)):
        now = q.popleft()
        if now == you:
            print(cnt-1)
            sys.exit(0)
        else:
            if now+1 <= 100000 and visited[now+1] == False:
                visited[now+1] = True
                q.append(now+1)
            if 0 <= now-1 and visited[now-1] == False:
                visited[now-1] = True
                q.append(now-1)
            if now < you and now*2 <= 100000 and visited[now*2] == False:
                visited[now*2] = True
                q.append(now*2)