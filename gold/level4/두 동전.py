#16197
def sol(l, x1, y1, x2, y2):
    global res
    if l == 11 or res < l:
        return
    coin1, coin2 = False, False
    if x1 < 0 or col <= x1 or y1 < 0 or row <= y1:
        coin1 = True
    if x2 < 0 or col <= x2 or y2 < 0 or row <= y2:
        coin2 = True
    if coin1 and coin2:
        return
    if coin1 or coin2:
        res = l
        return
    for k in range(4):
        xx1 = x1 + dx[k]
        xx2 = x2 + dx[k]
        yy1 = y1 + dy[k]
        yy2 = y2 + dy[k]
        if (xx1, yy1) in walls:
            xx1 = x1
            yy1 = y1
        if (xx2, yy2) in walls:
            xx2 = x2
            yy2 = y2
        if (xx1, yy1) == (xx2, yy2):
            continue
        if (x1, y1) == (xx1, yy1) and (x2, y2) == (xx2, yy2):
            continue
        sol(l+1, xx1, yy1, xx2, yy2)

row, col = map(int, input().split())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
walls = []
coins = []
res = float('inf')
for i in range(row):
    temp = list(input())
    for j, t in enumerate(temp):
        if t == '#':
            walls.append((j, i))
        if t == 'o':
            coins.append((j, i))

sol(0, coins[0][0], coins[0][1], coins[1][0], coins[1][1])

if res == float('inf'):
    print(-1)
else:
    print(res)
