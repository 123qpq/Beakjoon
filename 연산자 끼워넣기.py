#14888, 15658
import sys
def dfs(l, total, add, sub, mul, div):
    if l == n:
        res.append(total)
    else:
        if add:
            dfs(l+1, total+num[l], add-1, sub, mul, div)
        if sub:
            dfs(l+1, total-num[l], add, sub-1, mul, div)
        if mul:
            dfs(l+1, total * num[l], add, sub, mul-1, div)
        if div:
            if total < 0:
                dfs(l+1, -(-total // num[l]), add, sub, mul, div-1)
            else:
                dfs(l+1, total // num[l], add, sub, mul, div-1)

if __name__ == "__main__":
    n = int(input())
    num = list(map(int, input().split()))
    add, sub, mul, div = map(int, input().split())
    res = []
    dfs(1, num[0], add, sub, mul, div)
    print(max(res))
    print(min(res))