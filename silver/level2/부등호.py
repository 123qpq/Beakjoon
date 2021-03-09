#2529
def sol(l):
    if l == n:
        candidate.append(''.join(map(str, res)))
        return True
    else:
        for i in range(10):
            if lst[l] == '>' and res[-1] > i and i not in res:
                res.append(i)
                sol(l+1)
                res.pop()
            if lst[l] == '<' and res[-1] < i and i not in res:
                res.append(i)
                sol(l+1)
                res.pop()

n = int(input())
lst = list(input().split())
candidate = []
for i in range(10):
    res = [i]
    if sol(0):
        break
print(candidate[-1])
print(candidate[0])