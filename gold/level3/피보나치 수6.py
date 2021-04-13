#11444
#분할정복 개념
n = int(input())
arr = [[1, 1], [1, 0]]
res = [[1, 0], [0, 1]] # I

def div(a, b): #행렬곱
    temp = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                temp[i][j] += a[i][0] * b[0][j]
            temp[i][j] %= 1000000007
    return temp

while n:
    if n % 2 == 1: #홀수일 경우
        res = div(res, arr)
    arr = div(arr, arr)
    n //= 2

print(res[1][0])