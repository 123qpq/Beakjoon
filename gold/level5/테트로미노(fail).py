def sol(l, x, y, sum):
    global res
    if l == 4:
        if res < sum:
            res = sum
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < m and 0 <= yy < n and board[yy][xx] == 0:
                board[yy][xx] = 1
                sol(l+1, xx, yy, sum+table[yy][xx])
                board[yy][xx] = 0

n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
board = [[0]*m for _ in range(n)]
temp = [0, 0, 0, 0, 0]
res = 0
first = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for i in range(n):
    for j in range(m):
        if first <= table[i][j]:
            first = table[i][j]
            board[i][j] = 1
            sol(1, j, i, table[i][j])
            board[i][j] = 0
            if 1 < j < m-1:
                if i+1 < n:
                    temp = first + table[i+1][j-1] + table[i+1][j] + table[i+1][j+1]
                    if res < temp:
                        res = temp
                if 0 < i-1:
                    temp = first + table[i-1][j-1] + table[i-1][j] + table[i-1][j+1]
                    if res < temp:
                        res = temp
            if 1 < i < n-1:
                if j+1 < m:
                    temp = first + table[i-1][j+1] + table[i][j+1] + table[i+1][j+1]
                    if res < temp:
                        res = temp
                if 0 < j-1:
                    temp = first + table[i-1][j-1] + table[i][j-1] + table[i+1][j-1]
                    if res < temp:
                        res = temp
print(res)