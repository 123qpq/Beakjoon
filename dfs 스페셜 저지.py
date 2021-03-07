#16964
import sys

n = int(sys.stdin.readline())
lst = [[] for i in range(n+1)]
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    lst[a].append(b)
    lst[b].append(a)
answer = list(map(int, sys.stdin.readline().split()))

q = [1]
visited = [1]
rank = [-1 for i in range(n+1)]
res = []

for i in range(1, n+1):
    rank[answer[i-1]] = n+1-i

for i in range(1, n+1):
    lst[i] = sorted(lst[i], key=lambda x : rank[x])

while q:
    node = q.pop()
    res.append(node)

    for n in lst[node]:
        if n not in visited:
            visited.append(n)
            q.append(n)

if res == answer:
    print(1)
else:
    print(0)