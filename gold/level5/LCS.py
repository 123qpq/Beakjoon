#9251
import sys

a = list(sys.stdin.readline())
b = list(sys.stdin.readline())
table = [[0] * len(b) for _ in range(len(a))]

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i-1] == b[j-1]:
            table[i][j] = table[i-1][j-1] + 1
        else:
            table[i][j] = max(table[i-1][j], table[i][j-1])
print(table[-1][-1])