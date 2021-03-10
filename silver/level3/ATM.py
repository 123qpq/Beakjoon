#11399
n = int(input())
lst = list(map(int, input().split()))
res = 0
temp = 0
for l in sorted(lst):
    temp += l
    res += temp
print(res)