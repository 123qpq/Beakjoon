#15663
def bfs(level, permu):
    if level == m:
        for p in permu:
            print(p, end = ' ')
        print()
    else:
        check = 0
        for i in range(n):
            if res[i] == False and check != numlist[i]:
                res[i] = True
                listed.append(numlist[i])
                check = numlist[i]
                bfs(level+1, permu + [numlist[i]])
                res[i] = False
                listed.pop()

n, m = map(int, input().split())
res = [False] * n
listed = []
numlist = list(map(int, input().split()))
numlist.sort()
bfs(0, [])