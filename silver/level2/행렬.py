#1080
import sys

def change(i, j):
    for x in range(i, i+3):
        for y in range(j, j+3):
            A[x][y] = 1 - A[x][y]

cnt = 0
n, m = map(int, input().split())
A = [list(map(int, input())) for _ in range(n)]
B = [list(map(int, input())) for _ in range(n)]

for i in range(n-2):
    for j in range(m-2):
        if A[i][j] != B[i][j]:
            change(i, j)
            cnt += 1

for i in range(n):
    for j in range(m):
        if A[i][j] != B[i][j]:
            print(-1)
            sys.exit(0)
print(cnt)