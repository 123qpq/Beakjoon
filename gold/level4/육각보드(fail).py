#fail
import sys
n = int(input())
table = [['-']+ list(input()) + ['-'] for i in range(n)]
cnt = 0
beforeline = table.pop(0)

for i in range(n+2):
    if beforeline[i] == 'X': #첫줄에서 x가 발견되면
        cnt = max(cnt, 1)
        if beforeline[i+1] == 'X': #앞에 컬러가 사용됐으면
            cnt = 2 #최대 색상 2개

for nowline in table:
    for i in range(1, n+2):
        if nowline[i] == 'X':
            if beforeline[i] == 'X' or beforeline[i+1] == 'X':
                cnt = 2
                if beforeline[i] == 'X' and beforeline[i+1] == 'X': # 위, 위 뒤
                    print(3)
                    sys.exit(0)
            if beforeline[i-1] == 'X' and nowline[i+1] == 'X': #위 뒤, 뒤
                print(3)
                sys.exit(0)
            if nowline[i-1] == 'X': #앞에 컬러가 사용됐으면
                cnt = 2
    beforeline = nowline
print(cnt)

'''
#!/usr/bin/python3
import sys
sys.setrecursionlimit(1000000)
n = int(input())
a = [input() for _ in range(n)]
color = [[-1]*n for _ in range(n)]
dx = [-1,-1,0,0,1,1]
dy = [0,1,-1,1,-1,0]
ans = 0

def dfs(x, y, c):
    global ans
    color[x][y] = c
    ans = max(ans, 1)
    for k in range(6):
        nx, ny = x+dx[k], y+dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if a[nx][ny] == 'X':
                if color[nx][ny] == -1:
                    dfs(nx, ny, 1-c)
                ans = max(ans, 2)
                if color[nx][ny] == c:
                    ans = max(ans, 3)


for i in range(n):
    for j in range(n):
        if a[i][j] == 'X' and color[i][j] == -1:
            dfs(i, j, 0)

print(ans)
'''