#2580
def square(x, y):
    return (x//3)*3+(y//3)

def sol(z): #row-major-order
    if z == 81:
        for t in table:
            print(' '.join(map(str, t)))
        return True
    x = z // 9
    y = z % 9
    if table[x][y] != 0:
        return sol(z+1)
    else:
        for i in range(1, 10):
            if c1[x][i] == False and c2[y][i] == False and c3[square(x, y)][i] == False:
                c1[x][i] = c2[y][i] = c3[square(x, y)][i] = True
                table[x][y] = i
                if sol(z+1):
                    return True
                table[x][y] = 0
                c1[x][i] = c2[y][i]= c3[square(x, y)][i] = False
    return False

table = [list(map(int, input().split())) for _ in range(9)]
c1 = [[False]*10 for _ in range(9)]
c2 = [[False]*10 for _ in range(9)]
c3 = [[False]*10 for _ in range(9)]
for i in range(9):
    for j in range(9):
        if table[i][j] != 0:
            c1[i][table[i][j]] = True
            c2[j][table[i][j]] = True
            c3[square(i, j)][table[i][j]] = True
sol(0)