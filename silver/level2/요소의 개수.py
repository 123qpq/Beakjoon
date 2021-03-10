#11724
import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
dic = {i : [] for i in range(1, n+1)}
union = [True]*(n+1)
answer = 0
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    dic[x] += [y]
    dic[y] += [x]

def bfs(node):
    q = deque([node])
    while q:
        now = q.popleft()
        for i in dic[now]:
            if union[i]:
                q.append(i)
                union[i] = False

for i in range(1, n+1):
    if union[i]:
        union[i] = False
        bfs(i)
        answer += 1
print(answer)