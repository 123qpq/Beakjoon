#14500
import sys
shapeList = [[[0, 1], [0, 2], [0, 3]], # ㅡ
            [[1, 0], [2, 0], [3, 0]], # ㅣ
            [[0, 1], [1, 0], [1, 1]], 
            [[1, 0], [2, 0], [2, 1]],
            [[1, 0], [2, 0], [2, -1]],
            [[0, 1], [0, 2], [1, 0]],
            [[0, 1], [0, 2], [1, 2]],
            [[0, 1], [1, 1], [2, 1]],
            [[0, 1], [1, 0], [2, 0]],
            [[0, 1], [0, 2], [-1, 2]],
            [[1, 0], [1, 1], [1, 2]],
            [[1, 0], [1, 1], [2, 1]],
            [[1, 0], [1, -1], [2, -1]],
            [[0, 1], [-1, 1], [-1, 2]],
            [[0, 1], [1, 1], [1, 2]],
            [[0, 1], [0, 2], [1, 1]],
            [[1, 0], [1, 1], [2, 0]],
            [[1, 0], [1, -1], [2, 0]],
            [[0, 1], [0, 2], [-1, 1]]]

n, m = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
max_sumary = 0
sumary = 0
for i in range(n):
    for j in range(m):
        for shape in shapeList:
            sumary = table[i][j]
            for k in range(3):
                nX = j + shape[k][1]
                nY = i + shape[k][0]
                if 0 <= nX <= m-1 and 0 <= nY <= n-1:
                    sumary += table[nY][nX]

            if(max_sumary < sumary):
                max_sumary = sumary

print(max_sumary)