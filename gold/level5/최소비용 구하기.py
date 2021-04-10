#1916
import sys
import heapq
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
route = [[] for _ in range(n)]
cost = [float('inf')] * n
for _ in range(m):
    s, e, c = map(int, sys.stdin.readline().split())
    route[s-1].append((c, e-1))
go, to = map(int, sys.stdin.readline().split())

hq = []
cost[go-1] = 0
heapq.heappush(hq, (0, go-1))
while hq:
    length, node = heapq.heappop(hq)
    if cost[node] < length:
        continue
    for l, n in route[node]:
        l += length
        if l < cost[n]:
            cost[n] = l
            heapq.heappush(hq, (l, n))

print(cost[to-1])
