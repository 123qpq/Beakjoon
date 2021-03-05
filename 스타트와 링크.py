def coll(l, s):
    global res
    if l == team:
        start.sort()
        new = 0
        for i in range(team):
            for j in range(i+1, team):
                new += dic[(start[i], start[j])] - dic[(link[i], link[j])]
        if abs(new) < res:
            res = abs(new)
    else:
        for i in range(s, n):
            link.append(i)
            start.remove(i)
            coll(l+1, i+1)
            link.remove(i)
            start.append(i)

n = int(input())
team = n // 2
table = [list(map(int, input().split()))for _ in range(n)]
dic = {}
for i in range(n):
    for j in range(i+1, n):
        dic[(i, j)] = table[i][j] + table[j][i]

start = list(range(n))
link = []
res = float('inf')
coll(1, 1)
print(res)