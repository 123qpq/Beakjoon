#1865
import sys
tc = int(sys.stdin.readline())

def solution():
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for node, dist in graph[j]:
                if distlst[node] > dist + distlst[j]:
                    distlst[node] = dist + distlst[j]
                    if i == n:
                        return True
    return False

for _ in range(tc):
    n, m, w = map(int, sys.stdin.readline().split())
    graph = {x : [] for x in range(1, n+1)}

    for _ in range(m):
        s, e, t = map(int, sys.stdin.readline().split())
        graph[s].append((e, t))
        graph[e].append((s, t))

    for _ in range(w):
        s, e, t = map(int, sys.stdin.readline().split())
        graph[s].append((e, -t))
        
    distlst = [9999999]*(n+1)

    if solution():
        print("YES")
    else:
        print("NO")