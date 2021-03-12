#11723
import sys
n = int(sys.stdin.readline())
bit = 0
for _ in range(n):
    temp = sys.stdin.readline().split()
    if temp[0] == "all":
        bit = (1 << 21) - 1
    elif temp[0] == "empty":
        bit = 0
    else:
        order, num = temp[0], temp[1]
        num = int(num)

        if order == "add":
            bit |= (1 << num)
        elif order == "remove":
            bit &= ~(1 << num)
        elif order == "check":
            if bit & (1 << num) == 0:
                print(0)
            else:
                print(1)
        elif order == "toggle":
            bit = bit ^ (1 << num)