import sys
#10830
n, b = map(int, sys.stdin.readline().split())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


def sol(mat, b):
    if b == 1:
        return mat
    else:
        if b%2:
            ans = sol(mat, b-1)
            temp = [[sum(a*b for a, b in zip(row, col))%1000 for col in zip(*ans)] for row in mat]
        else:
            ans = sol(mat, b//2)
            temp = [[sum(a*b for a, b in zip(row, col))%1000 for col in zip(*ans)] for row in ans]
    return temp

for row in sol(mat, b):
    
    print(' '.join(map(lambda x : str(x%1000), row)))