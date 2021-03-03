#14225
import sys
def dfs(l, total):
    if l == n:
        if total != 0:
            temp.append(total)
    else:
        dfs(l+1, total)
        dfs(l+1, total+lst[l])

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
temp = []
dfs(0, 0)
temp = sorted(set(temp))
for idx, t in enumerate(temp):
    if idx+1 != t:
        print(idx+1)
        break
else:
    print(len(temp)+1)