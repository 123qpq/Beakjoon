#16198
def sol(l, sum, lst):
    global res
    if l == n-2:
        if res < sum:
            res = sum
    else:
        for i in range(1, len(lst)-1):
            sol(l+1, lst[i-1] * lst[i+1] + sum, lst[:i] + lst[i+1:])

n = int(input())
energy = list(map(int, input().split()))
res = 0
sol(0, 0, energy)
print(res)