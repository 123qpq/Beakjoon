#1764
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
lst1 = [input()[:-1] for _ in range(n)]
lst2 = [input()[:-1] for _ in range(m)]
res = set(lst1) & set(lst2)
print(len(res))
for r in sorted(res):
    print(r)