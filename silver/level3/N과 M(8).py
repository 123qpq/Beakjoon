#15657
def bfs(level, permu):
    if level == m:
        for p in permu:
            print(p, end = ' ')
        print()
    else:
        for i in range(n):
            if numlist[i] < permu[-1]:
                continue
            bfs(level+1, permu + [numlist[i]])

n, m = map(int, input().split())
numlist = list(map(int, input().split()))
numlist.sort()
for i in range(n):
    bfs(1, [numlist[i]])