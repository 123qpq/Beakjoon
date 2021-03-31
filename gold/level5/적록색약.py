#10026
import sys
sys.setrecursionlimit(100000)
def search(y, x, color):
    if table[y][x] != color or check[y][x] == True:
        return
    else:
        check[y][x] = True
        if table[y][x] == 'G':
            table[y][x] = 'R'
        for i in range(4):
            dxx = x + dx[i]
            dyy = y + dy[i]
            if 0 <= dxx < n and 0 <= dyy < n:
                search(dyy, dxx, color)

n = int(sys.stdin.readline())
table = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
check = [[False]*n for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
cnt = 0
cnt2 = 0
for i in range(n):
    for j in range(n):
        if check[i][j] == False:
            search(i, j, table[i][j])
            cnt += 1
print(cnt, end = ' ')

check = [[False]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if check[i][j] == False:
            search(i, j, table[i][j])
            cnt2 += 1
print(cnt2)
