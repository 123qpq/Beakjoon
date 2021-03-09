#2667
def bfs(x, y):
    global cnt
    cnt += 1
    table[y][x] = 0
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and table[yy][xx] == 1:
            bfs(xx, yy)

n = int(input())
table = [list(map(int, input())) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
lst = []
for i in range(n):
    for j in range(n):
        if table[i][j] == 1:
            cnt = 0
            bfs(j, i)
            lst.append(cnt)
print(len(lst))
for l in sorted(lst):
    print(l)