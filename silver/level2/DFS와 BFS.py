#1260
import sys
from collections import deque
n, v, m = map(int, sys.stdin.readline().split())
tree = [[0]*(n+1) for _ in range(n+1)]
visited = [True] * (n+1)
for _ in range(v):
    x, y = map(int, sys.stdin.readline().split())
    tree[x][y] = 1
    tree[y][x] = 1

def dfs(node):
    visited[node] = False
    print(node, end = ' ')
    for i in range(1, n+1):
        if visited[i] and tree[node][i] == 1:
            dfs(i)

dfs(m)
print()
q = deque([m])
visited[m] = True
print(m, end = ' ')
while q:
    for _ in range(len(q)):
        node = q.popleft()
        for i in range(1, n+1):
            if not visited[i] and tree[node][i] == 1:
                visited[i] = True
                q.append(i)
                print(i, end=' ')