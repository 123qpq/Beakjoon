#1780
import sys

def sol(x, y, n):
    pv = table[y][x]
    breakcheck = False
    for i in range(x, x+n):
        if breakcheck: #2중 탈출
            break
        for j in range(y, y+n):
            if table[j][i] != pv:
                mini = n//3
                #9분할 탐색
                sol(x, y, mini)
                sol(x+mini, y, mini)
                sol(x+2*mini, y, mini)
                sol(x, y+mini, mini)
                sol(x+mini, y+mini, mini)
                sol(x+2*mini, y+mini, mini)
                sol(x, y+2*mini, mini)
                sol(x+mini, y+2*mini, mini)
                sol(x+2*mini, y+2*mini, mini)

                breakcheck = True
                break

    if not breakcheck:
        answer[pv+1] += 1

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    table = [list(map(int, sys.stdin.readline().split()))for _ in range(n)]
    answer = [0, 0, 0]
    pv = table[0][0]
    sol(0, 0, n)

    for a in answer:
        print(a)
