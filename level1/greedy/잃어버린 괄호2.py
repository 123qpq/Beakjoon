#1541
exp = input().split('-')
numlst = []
for e in exp:
    numlst.append(sum(map(int, e.split('+'))))
res = numlst[0] - sum(numlst[1:])
print(res)