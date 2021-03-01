n, l = map(int, input().split())
for i in range(l, 101):
    if i % 2 == 1 and n % i == 0:
        temp = n//i - (i-1)//2
        if temp < 0:
            print(-1)
            break
        for x in range(i):
            print(temp + x, end = ' ')
        break
    elif i % 2 == 0 and n / i - int(n/i)== 0.5:
        temp = int(n/i-0.5) - (i//2-1)
        if temp < 0:
            print(-1)
            break
        for x in range(i):
            print(temp + x, end = ' ')
        break
else:
    print(-1)