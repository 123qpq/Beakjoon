#11403
import sys
n = int(sys.stdin.readline())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if table[i][j] == 1:
            q = [j]
            while q:
                node = q.pop()
                for k in range(n):
                    if table[node][k] == 1 and table[i][k] != 1:
                        table[i][k] = 1
                        q.append(k)
for t in table:
    for x in t:
        print(x, end = ' ')
    print()