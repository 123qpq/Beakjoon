#1238
import sys
import heapq
n, m, x = map(int, sys.stdin.readline().split())
table = [[] for _ in range(n)]
dist = [float('inf')]*n
dist[x-1] = 0

for _ in range(m):
    p1, p2, c = list(map(int, sys.stdin.readline().split()))
    table[p1-1].append((c, p2-1))

hq = []
heapq.heappush(hq, (0, x-1))

while hq:
    d, now = heapq.heappop(hq)
    if dist[now] < d:
        continue
    
    for next_dist, next_node in table[now]:
        cost = dist[now] + next_dist
        if cost < dist[next_node]:
            dist[next_node] = cost
            heapq.heappush(hq, (cost, next_node))

for j in range(n):
    if j == x-1:
        continue
    
    dist2 = [float('inf')]*n
    dist2[j] = 0
    heapq.heappush(hq, (0, j))
    
    while hq:
        d, now = heapq.heappop(hq)
        if dist2[x-1] < d:
            continue
        
        for next_dist, next_node in table[now]:
            cost = dist2[now] + next_dist
            if cost < dist2[next_node] and cost < dist2[x-1]:
                dist2[next_node] = cost
                heapq.heappush(hq, (cost, next_node))
    dist[j] += dist2[x-1]
print(max(dist))