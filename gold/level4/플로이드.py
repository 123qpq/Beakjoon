#11404
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
buslines = [[float('inf')]*n for _ in range(n)]
for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    if buslines[start-1][end-1] > cost:
        buslines[start-1][end-1] = cost
for k in range(n):
    buslines[k][k] = 0
    for i in range(n):
        for j in range(n):
            buslines[i][j] = min(buslines[i][j], buslines[i][k] + buslines[k][j])

for busline in buslines:
    for i in range(n):
        if busline[i] == float('inf'):
            print(0, end = ' ')
        else:
            print(busline[i], end = ' ')
    print()