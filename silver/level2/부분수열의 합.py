#1182
import sys
def dfs(l, total):
    global cnt
    if l == n:
        if s == total:
            cnt += 1
    else:
        dfs(l+1, total)
        dfs(l+1, total+lst[l])

n, s = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
cnt = 0
dfs(0, 0)
if s == 0:
    cnt -= 1
print(cnt)