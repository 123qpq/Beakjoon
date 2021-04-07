import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
sol = sys.stdin.readline()
answer = 0
check = 0
i = 1
while i < m-1:
    if sol[i-1] == 'I' and sol[i] == 'O' and sol[i+1] == 'I':
        check += 1
        if check == n:
            check -= 1
            answer += 1
        i += 1
    else:
        check = 0
    i += 1
print(answer)