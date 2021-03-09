#1655
import heapq
import sys
n = int(sys.stdin.readline())
left, right = [], []
for _ in range(n):
    num = int(sys.stdin.readline())

    if len(left) == len(right):
        heapq.heappush(left, (-num, num))
    else:
        heapq.heappush(right, (num, num))
    
    if right and left[0][1] > right[0][1]:
        ltemp = heapq.heappop(left)[1]
        rtemp = heapq.heappop(right)[1]
        heapq.heappush(right, (ltemp, ltemp))
        heapq.heappush(left, (-rtemp, rtemp))
    
    print(left[0][1])


''' time error code...
import sys
import bisect
n = int(sys.stdin.readline())
lst = []
for i in range(n):
    num = int(sys.stdin.readline())
    bisect.insort(lst, num)
    print(lst[(i)//2])
'''