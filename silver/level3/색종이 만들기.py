def search(half, table):
    global blue, white
    if half == 0:
        print()
    else:
        for i in range(4):
            for j in range(half):
                for k in range(half-1):
                    if table[j][k] != table[j][k+1]:
                        
    

n = int(input())
table = [int(input()) for _ in range(n)]
blue = 0
white = 0
search(n//2, table)
