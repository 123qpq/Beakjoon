#9205
import sys
from collections import deque
n = int(sys.stdin.readline())
for _ in range(n):
    mcount = int(sys.stdin.readline())
    q = deque([tuple(map(int, sys.stdin.readline().split()))])
    marts = {}
    for _ in range(mcount):
        marts[tuple(map(int, sys.stdin.readline().split()))] = False
    festival = tuple(map(int, sys.stdin.readline().split()))
    
    while q:
        now = q.popleft()
        if abs(festival[0]-now[0])+abs(festival[1]-now[1]) <= 1000:
                print("happy")  
                break
        else:
            for mart in marts:
                if marts[mart] == False and abs(mart[0]-now[0])+abs(mart[1]-now[1]) <= 1000:
                    marts[mart] = True
                    q.append(mart)
    else:
        print("sad")