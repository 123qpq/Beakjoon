#1541
exp = input()
num = ''
numlst = []
signlst = []
for e in exp:
    if e.isdecimal():
        num += e
    else:
        numlst.append(int(num))
        num = ''
        signlst.append(e)
numlst.append(int(num))
for i in reversed(range(len(signlst))):
    if signlst[i] == '+':
        numlst[i] += numlst[i+1]
        numlst[i+1] = 0
res = numlst[0]
for i in range(1, len(numlst)):
    res -= numlst[i]
print(res)