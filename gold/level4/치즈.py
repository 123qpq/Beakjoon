#2638
import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dq = deque([(0, 0)])
answer = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def sol():
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
                
def melting():
    temp = True
    for i in range(n):
        for j in range(m):
            if table[i][j] == 0:
                continue
            elif table[i][j] > 2:
                table[i][j] = 0
                visited[i][j] = True
                dq.append((j, i))
        if False in visited[i]:
            temp = False
    return temp

while True:
    answer += 1
    sol()
    if melting():
        break
print(answer)