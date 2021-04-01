#9461
import sys
tc = int(sys.stdin.readline())
lst = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for _ in range(tc):
    n = int(sys.stdin.readline())
    if n-1 < len(lst):
        print(lst[n-1])
    else:
        for _ in range(n-len(lst)):
            temp = lst[-1] + lst[-5]
            lst.append(temp)
        print(lst[-1])