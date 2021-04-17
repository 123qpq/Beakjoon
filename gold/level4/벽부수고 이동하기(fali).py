import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
table = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

count = 0
dq = deque([(0, 0, 1)])
while dq:
    count += 1
    for _ in range(len(dq)):
        x, y, block = dq.popleft()
        print(x, y, block)
        if x == m-1 and y == n-1:
            print(count)
            sys.exit(0)
        else:
            table[y][x] = False
            for i in range(4):
                dxx = x + dx[i]
                dyy = y + dy[i]
                if 0 <= dxx < m and 0 <= dyy < n and table[dyy][dxx] != False:
                    if table[dyy][dxx] == '0':
                        print(dxx, dyy)
                        dq.append((dxx, dyy, block))
                    elif block == 1:
                        dq.append((dxx, dyy, block-1))
print(-1)