#16929
import sys
def cicle(x, y, purpose):
    for c in range(4):
        xx = x + dx[c]
        yy = y + dy[c]
        if 0 <= xx < col and 0 <= yy < row and table[yy][xx] == purpose:
            if visited[yy][xx] == True:
                if yy == i and xx == j-1 and x != j and y != i:
                    visited[y][x] = True
                    print("Yes")
                    sys.exit(0)
                continue
            else:
                visited[y][x] = True
                cicle(xx, yy, purpose)
                visited[y][x] = False

row, col = map(int, input().split())
table = [list(input()) for _ in range(row)]
visited = [[False]*col for _ in range(row)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for i in range(row):
    for j in range(1, col):
        if table[i][j] == table[i][j-1]:
            visited[i][j-1] = True
            cicle(j, i, table[i][j])
            visited[i][j-1] = False
print("No")