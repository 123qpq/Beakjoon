#5639
import sys
import bisect
sys.setrecursionlimit(100000000)

def sol(start, end):
    if start > end:
        return
    
    right = bisect.bisect_left(tree, tree[start], start+1, end+1)
    sol(start+1, right-1) #왼쪽
    sol(right, end) #오른쪽
    print(tree[start]) #루트출력

tree = []
count = 0
while count <= 10000:
    try:
        temp = int(input())
    except:
        break
    tree.append(temp)
    count += 1
sol(0, len(tree)-1)