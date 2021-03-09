#1003
tc = int(input())
table = []
table.append((1, 0))
table.append((0, 1))
for _ in range(39):
    a, b = table[-1]
    c, d = table[-2]
    table.append((a+c, b+d))
for _ in range(tc):
    n = int(input())
    print(table[n][0], table[n][1])