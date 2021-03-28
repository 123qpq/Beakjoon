#9375
import sys
n = int(sys.stdin.readline())
for _ in range(n):
    wears = int(sys.stdin.readline())
    closet = {}
    for _ in range(wears):
        wear, idx = sys.stdin.readline().split()
        closet[idx] = closet.get(idx, []) + [wear]
    count = 1
    for idx in closet:
        count *= len(closet[idx])+1
    print(count-1)