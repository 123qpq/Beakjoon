import sys

n, m = map(int, sys.stdin.readline().split())
met = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
#answer = [[1 if i==j else 0 for i in range(n)] for j in range(n)]
answer = [met[i] for i in range(n)]

def make_mat(a, b):
    return [[sum(a*b for a, b in zip(row, col))%1000 for col in zip(*a)] for row in b]

if m % 2:
    m -= 1
    while m != 0:
        temp = met[:]
    if m % 2:
        answer = make_mat(answer, met)
        m -= 1
    else:
        answer = make_mat(answer, answer)
        m //= 2
    print(answer, m)
else:
    m *= 2
    while m >= 2:
        temp = met[:]
    if m % 2:
        answer = make_mat(answer, met)
        m -= 1
    else:
        answer = make_mat(answer, answer)
        m //= 2
    print(answer, m)


for ans in answer:
    for a in ans:
        print(a, end = ' ')
    print()