#1643
n = int(input())
cnt = 0
lst = [0, 0, 1, 1] + [0]*(n-3)

for i in range(4, n+1):
    lst[i] = lst[i-1]+1
    if i % 3 == 0 and lst[i//3]+1< lst[i]:
        lst[i] = lst[i//3] + 1
    if i % 2 == 0 and lst[i//2]+1 < lst[i]:
        lst[i] = lst[i//2] + 1
print(lst[n])