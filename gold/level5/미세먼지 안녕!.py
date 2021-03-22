import sys
def get_aircleaner():
    for i in range(row):
        if table[i][0] == -1:
            return i, i+1

def spread_dust():
    temp = [[0]*col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            if 5 <= table[i][j]:
                dif = table[i][j] // 5
                if 0 <= i - 1 and table[i-1][j] != -1: # 위
                    temp[i-1][j] += dif
                    table[i][j] -= dif
                if 0 <= j - 1 and table[i][j-1] != -1: # 왼쪽
                    temp[i][j-1] += dif
                    table[i][j] -= dif
                if i+1 < row and table[i+1][j] != -1: # 아래
                    temp[i+1][j] += dif
                    table[i][j] -= dif
                if j+1 < col and table[i][j+1] != -1: # 오른쪽
                    temp[i][j+1] += dif
                    table[i][j] -= dif
                
    for i in range(row):
        for j in range(col):
            table[i][j] += temp[i][j]

def aircleaner_on():
    #up 공기청소기
    for i in range(1, up): #첫줄 밀어내기
        table[up-i][0] = table[up-i-1][0]
    for j in range(col-1): #윗줄 밀어내기
        table[0][j] = table[0][j+1]
    for i in range(up): #끝줄 밀어내기
        table[i][col-1] = table[i+1][col-1]

    #dwon 공기청소기
    for i in range(down+1, row-1): #첫줄 밀어내기
        table[i][0] = table[i+1][0]
    for j in range(col-1): #밑줄 밀어내기
        table[row-1][j] = table[row-1][j+1]
    for i in range(1, row-down): #끝줄 밀어내기
        table[row-i][col-1] = table[row-i-1][col-1]

    for j in range(1, col): #가운데 줄 동시에 밀어내기
        table[up][col-j] = table[up][col-j-1]
        table[down][col-j] = table[down][col-j-1]
    table[up][1] = table[down][1] = 0


    
if __name__ == "__main__":
    row, col, time = map(int, sys.stdin.readline().split())
    table = [list(map(int, sys.stdin.readline().split())) for _ in range(row)]
    up, down = get_aircleaner()

    for _ in range(time):
        spread_dust()
        aircleaner_on()
    res = 0
    for t in table:
        res += sum(t)
    print(res+2)