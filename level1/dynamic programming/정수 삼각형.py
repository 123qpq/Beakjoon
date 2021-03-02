#1932
n = int(input())
tri = [0]*n
for _ in range(n):
    temp = list(map(int, input().split()))
    for i in range(len(temp)-1, 0, -1):
        if tri[i] > tri[i-1]:
            tri[i] += temp[i]
        else:
            tri[i] = tri[i-1] + temp[i]
    tri[0] += temp[0]
print(max(tri))