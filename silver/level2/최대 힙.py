#11279
import heapq
import sys
n = int(sys.stdin.readline())
lst = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(lst, (-num, num))
    elif len(lst) != 0:
        print(heapq.heappop(lst)[1])
    else:
        print(0)