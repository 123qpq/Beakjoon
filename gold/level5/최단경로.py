#1753
import sys
import heapq

nodes, e = map(int, sys.stdin.readline().split())
route = [float('inf')] * (nodes)
start = int(sys.stdin.readline()) - 1
graph = [[] for _ in range(nodes)]

for _ in range(e):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u-1].append((w, v-1))

hq = []
route[start] = 0
heapq.heappush(hq, (0, start))

while hq:
    length, node = heapq.heappop(hq)
    if route[node] < length:
        continue
    for l, n in graph[node]:
        l += length
        if l < route[n]:
            route[n] = l
            heapq.heappush(hq, (l, n))

for i in range(nodes):
    print(route[i] if route[i] != float('inf') else 'INF')