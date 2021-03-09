#11060
import sys
n = int(input())
if n == 1:
    print(0)
    sys.exit()
lst = list(map(int, input().split()))
dy = [0] + [float('inf')]*(n-1)
for i in range(n-1):
    for j in range(lst[i]):
        if i+j+1 > n-1:
            break
        if dy[i+j+1] == float('inf'):
            dy[i+j+1] = dy[i]+1
            if dy[n-1] != float('inf'):
                print(dy[n-1])
                sys.exit(0)
print(-1)