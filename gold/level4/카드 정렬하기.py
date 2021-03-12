#1715
import sys
import heapq
n = int(sys.stdin.readline())
cards = []
for _ in range(n):
    heapq.heappush(cards, int(sys.stdin.readline()))

if n == 1:
    print(0)
else:
    res = 0
    while len(cards) > 1:
        a = heapq.heappop(cards)
        b = heapq.heappop(cards)
        res += a + b
        heapq.heappush(cards, a+b)
    print(res)