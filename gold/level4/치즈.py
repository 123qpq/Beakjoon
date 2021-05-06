#2638
import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def sol():
    visited = [[False]*m for _ in range(n)]
    dq = deque([(0, 0)])
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            dxx = x + dx[i]
            dyy = y + dy[i]
            if (0 <= dyy < n) and (0 <= dxx < m) and visited[dyy][dxx] == False:
                if table[dyy][dxx] != 0:
                    table[dyy][dxx] += 1
                else:
                    visited[dyy][dxx] = True
                    dq.append((dxx, dyy))
                
def cleaning():
    temp = (0, 0)
    for i in range(n):
        for j in range(m):
            if table[i][j] == 0:
                continue
            elif table[i][j] > 2:
                temp = (j, i)
                table[i][j] = 0
            else:
                table[i][j] = 1
    return temp

while True:
    sol()
    if cleaning() == (0, 0):
        break
    answer += 1
print(answer)