import sys
n, m = map(int, sys.stdin.readline().split())
dic = {}
for _ in range(n):
    a, b = sys.stdin.readline().split()
    dic[a] = b
for _ in range(m):
    print(dic[sys.stdin.readline().rstrip()])