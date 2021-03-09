#1927
import sys
import heapq
n = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(n)]
hq = []
for i in lst:
    if i == 0:
        if len(hq) == 0:
            print(0)
        else:
            print(heapq.heappop(hq))
    else:
        heapq.heappush(hq, i)