#11286
import sys
import heapq
n = int(sys.stdin.readline().rstrip())
minus = []
plus = []
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    if num > 0:
        heapq.heappush(plus, num)
    elif num < 0:
        heapq.heappush(minus, abs(num))
    else:
        if plus and minus:
            if plus[0] < minus[0]:
                print(heapq.heappop(plus))
            else:
                print(-heapq.heappop(minus))
        elif plus and not minus:
            print(heapq.heappop(plus))
        elif not plus and minus:
            print(-heapq.heappop(minus))
        else:
            print(0)