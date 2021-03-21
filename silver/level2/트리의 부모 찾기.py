#11725
import sys
n = int(sys.stdin.readline())
tree = {x : [] for x in range(1, n+1)}
ans = [0] * (n+1)
for _ in range(n-1):
    x, y = map(int, sys.stdin.readline().split())
    tree[x].append(y)
    tree[y].append(x)

q = [1]
while q:
    now = q.pop()
    for child in tree[now]:
        if ans[child] == 0:
            ans[child] = now
            q.append(child)
for a in ans[2:]:
    print(a)