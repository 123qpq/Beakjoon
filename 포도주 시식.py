#2156
n = int(input())
wines = [int(input()) for _ in range(n)]
a, b, c = 0, 0, 0
for i in wines:
    a, b, c = max(a, b, c), a+i, b+i

print(max(a, b, c))