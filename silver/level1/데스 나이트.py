#16948
import sys
from collections import deque

n = int(sys.stdin.readline())
knights = list(map(int, sys.stdin.readline().split()))
visited = [[False]*n for _ in range(n)]
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

cnt = 0
q = deque()
q.append((knights[0], knights[1]))

if abs(knights[0]- knights[2]) % 2 != 0:
    print(-1)
    sys.exit(0)

while q:
    cnt += 1

    for _ in range(len(q)):
        now = q.popleft()
        for i in range(6):
            dxx = now[0] + dx[i]
            dyy = now[1] + dy[i]
            if dxx == knights[2] and dyy == knights[3]:
                print(cnt)
                sys.exit(0)
            if 0 <= dxx < n and 0 <= dyy < n and visited[dxx][dyy] == False:
                visited[dxx][dyy] = True
                q.append((dxx, dyy))
print(-1)