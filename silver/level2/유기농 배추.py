#1012
import sys
sys.setrecursionlimit(1000000)

def search(i, j):
    table[i][j] = 0
    if i+1 <= n-1 and table[i+1][j] == 1:
        search(i+1, j)
    if 0 <= i-1 and table[i-1][j] == 1:
        search(i-1, j)
    if j+1 <= m-1 and table[i][j+1] == 1:
        search(i, j+1)
    if 0 <= j-1 and table[i][j-1] == 1:
        search(i, j-1)

tc = int(sys.stdin.readline())
for _ in range(tc):
    cnt = 0
    m, n, k = map(int, sys.stdin.readline().split())
    table = [[0]*m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        table[y][x] = 1

    for i in range(n):
        for j in range(m):
            if table[i][j] == 1:
                search(i, j)
                cnt += 1
    print(cnt)