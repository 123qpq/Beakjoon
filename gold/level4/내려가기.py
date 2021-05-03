#2096
import sys
n = int(sys.stdin.readline())
mint = maxt = list(map(int, sys.stdin.readline().split()))

for _ in range(1, n):
    temp = list(map(int, sys.stdin.readline().split()))
    mint = [min(mint[0], mint[1]) + temp[0],\
        min(mint)+ temp[1], min(mint[1], mint[2]) + temp[2]]
    maxt = [max(maxt[0], maxt[1]) + temp[0],\
        max(maxt)+temp[1], max(maxt[1], maxt[2]) + temp[2]]
print(max(maxt), min(mint))