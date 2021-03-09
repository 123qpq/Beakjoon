#1149
import sys
n = int(sys.stdin.readline())
houses = [list(map(int, sys.stdin.readline().split()))]
for i in range(1, n):
    houses.append(list(map(int, sys.stdin.readline().split())))
    houses[i][0] += min(houses[i-1][1], houses[i-1][2])
    houses[i][1] += min(houses[i-1][0], houses[i-1][2])
    houses[i][2] += min(houses[i-1][0], houses[i-1][1])
print(min(houses[-1]))