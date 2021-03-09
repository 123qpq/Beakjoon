#7576
import sys
from collections import deque
x, y = map(int, input().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(y)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
q = deque()
for i in range(y):
    for j in range(x):
        if table[i][j] == 1:
            q.append(((j, i)))
cnt = 0
while q:
    cnt += 1
    for _ in range(len(q)):
        now = q.popleft()
        for i in range(4):
            xx = now[0] + dx[i]
            yy = now[1] + dy[i]
            if 0 <= xx < x and 0 <= yy < y and table[yy][xx] == 0:
                table[yy][xx] = 1
                q.append((xx, yy))
for t in table:
    if 0 in t:
        print(-1)
        sys.exit(0)
print(cnt-1)