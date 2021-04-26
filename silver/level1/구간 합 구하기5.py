#11660
import sys

n, m = map(int, sys.stdin.readline().split())
table = [[0] * (n+1)]

for _ in range(n):
    table.append([0] + list(map(int, sys.stdin.readline().split())))

for i in range(1, n+1):
    for j in range(1, n):
        table[i][j+1] += table[i][j]

for i in range(1, n):
    for j in range(1, n+1):
        table[i+1][j] += table[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())    
    print(table[x2][y2] - table[x1-1][y2] - table[x2][y1-1] + table[x1-1][y1-1])