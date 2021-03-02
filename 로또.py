#6603
def dfs(l, s):
    if l == 6:
        for i in range(6):
            print(lst[i], end = ' ')
        print()
    else:
        for i in range(s, n):
            lst[l] = temp[i]
            dfs(l+1, i+1)

while True:
    n, *temp = list(map(int, input().split()))
    lst = [0] * n
    dfs(0, 0)
    if n == 0:
        break
    print()