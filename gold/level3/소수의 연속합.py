#1644
n = int(input())
lst = [False, False] + [True] * (n-1)
nlist = []
for i in range(2, n+1):
    if lst[i]:
        nlist.append(i)
        for j in range(2*i, n+1, i):
            lst[j] = False
lenn = len(nlist)
start = 0
total = 0
end = 0
cnt = 0
while end < lenn:
    total += nlist[end]
    while n < total:
        total -= nlist[start]
        start += 1
    if total == n:
        cnt +=1
    end += 1
print(cnt)