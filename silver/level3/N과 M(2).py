#15650
def bfs(level, num):
    if level == m:
        for x in res:
            print(x , end = " ")
        print()
    else:
        for j in range(num+1, n+1):
            res.append(j)
            bfs(level+1, j)
            res.pop()

n, m = map(int, input().split())
res = []
for i in range(1, n-m+2):
    res.append(i)
    bfs(1, i)
    res.pop()