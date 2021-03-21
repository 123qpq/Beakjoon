#15652
import sys
def bfs(level, ans):
    if level == m:
        for a in ans:
            print(a, end = ' ')
        print()
    else:

        for i in range(ans[-1], n+1):
            bfs(level+1, ans + [i])


n, m = map(int, sys.stdin.readline().split())
for i in range(1, n+1):
    bfs(1, [i])