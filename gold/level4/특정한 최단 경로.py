#1504
import sys
import heapq
n, e = map(int, sys.stdin.readline().split())
table = [[] for _ in range(n)]
hq = []

for _ in range(e):
    p1, p2, c = list(map(int, sys.stdin.readline().split()))
    table[p1-1].append((c, p2-1))
    table[p2-1].append((c, p1-1))

v1, v2 = map(int, sys.stdin.readline().split())

def dstra(start):
    dist = [float('inf')]*n
    dist[start] = 0
    heapq.heappush(hq, (0, start))

    while hq:
        d, now = heapq.heappop(hq)
        if dist[now] < d:
            continue
        
        for next_dist, next_node in table[now]:
            cost = dist[now] + next_dist
            if cost < dist[next_node]:
                dist[next_node] = cost
                heapq.heappush(hq, (cost, next_node))
    return dist

from_0 = dstra(0)
from_v1 = dstra(v1-1)
from_v2 = dstra(v2-1)

a = from_0[v1-1] + from_v1[v2-1] + from_v2[n-1] # 0~v1, v1~v2, v2~n
b = from_0[v2-1] + from_v2[v1-1] + from_v1[n-1] # 0~v2, v2~v1, v1~n
answer = min(a, b)
if answer != float('inf'):
    print(answer)
else:
    print(-1)