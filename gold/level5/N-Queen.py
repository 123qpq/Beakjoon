#9663
def nqueen(sol, lenn):
    global cnt
    if lenn == n:
        cnt += 1
    else:
        candidate = list(range(n))
        for i in range(lenn):
            comp = sol[i]
            if comp in candidate:
                candidate.remove(comp)
            distance = lenn - i
            if comp + distance in candidate: # 대각선
                candidate.remove(comp + distance)
            if comp - distance in candidate: # 대각선
                candidate.remove(comp - distance)
        if candidate != []: #넣을 수 있는 자리 존재
            for j in candidate:
                nqueen(sol + [j], lenn+1)

n = int(input())
cnt = 0
for i in range(n):
    nqueen([i], 1)
print(cnt)