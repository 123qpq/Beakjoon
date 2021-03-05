#14889
def coll(l):
    global res
    if l == team:
        starts = 0
        links = 0
        for i in range(n):
            for j in range(i+1, n):
                if i in link and j in link:
                    links += dic[(i, j)]
                if i not in link and j not in link:
                    starts += dic[(i, j)]
        if abs(starts-links) < res:
            res = abs(starts-links)
    else:
        for i in range(l, n):
            link.append(i)
            coll(l+1)
            link.remove(i)

n = int(input())
team = n // 2
table = [list(map(int, input().split()))for _ in range(n)]
dic = {}
for i in range(n):
    for j in range(i+1, n):
        dic[(i, j)] = table[i][j] + table[j][i]

link = [0]
res = float('inf')
coll(1)
print(res)