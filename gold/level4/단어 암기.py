#fail...
import sys

n, m = map(int, sys.stdin.readline().split())
words = [sys.stdin.readline().rstrip() for _ in range(n)]
check = [[] for _ in range(n)]
cnt = n

for _ in range(m):
    pv, alpha = sys.stdin.readline().split()
    if pv == '1':
        for i in range(n):
            if alpha in words[i]:
                if len(check[i]) == 0:
                    cnt -= 1
                check[i].append(alpha)
    else:
        for i in range(n):
            if alpha in check[i]:
                check[i].remove(alpha)
                if len(check[i]) == 0:
                    cnt += 1
    print(cnt)