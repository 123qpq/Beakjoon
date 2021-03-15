#15654
def bfs(level, permu):
    if level == m:
        for p in permu:
            print(p, end = ' ')
        print()
    else:
        for i in range(n):
            if res[i] == False:
                res[i] = True
                bfs(level+1, permu + [numlist[i]])
                res[i] = False

n, m = map(int, input().split())
res = [False] * n
numlist = list(map(int, input().split()))
numlist.sort()
bfs(0, [])