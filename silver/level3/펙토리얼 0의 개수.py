n = int(input())
cnt5 = 0
for i in range(5, n+1):
    while i % 5 == 0:
        cnt5 += 1
        i //= 5
print(cnt5)