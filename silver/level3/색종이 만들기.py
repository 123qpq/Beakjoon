#1167
import sys
def check(x, y, length):
    pv = table[y][x]
    for i in range(y,y+length):
        for j in range(x, x+length):
            if table[i][j] != pv:
                return False
    return True

def find(x, y, length):
    if check(x, y, length):
        res[table[y][x]] += 1
    else:
        length //= 2
        find(x, y, length)
        find(x, y+length, length)
        find(x+length, y, length)
        find(x+length, y+length, length)
        return

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    res = [0, 0]
    find(0, 0, n)
    for i in res:
        print(i)