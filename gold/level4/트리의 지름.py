#1967
import sys
from collections import deque
def bfs(node):
    finalnode, total = 0, 0
    q = deque([(node, 0)])
    while q:
        nextnode, dis = q.popleft()
        for i in dic[nextnode]:
            if visited[i[0]] == False:
                visited[i[0]] = True
                q.append((i[0], i[1]+dis))
                if total < i[1]+dis:
                    total = i[1]+dis
                    finalnode = i[0]
    return finalnode, total

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    if n == 1:
        print(0)
        sys.exit(0)
    dic = {}
    visited = [False] * (n+1)
    ans = 0
    
    for _ in range(n-1):
        parent, child, length = map(int, sys.stdin.readline().split())
        dic[parent] = dic.get(parent, []) + [(child, length)]
        dic[child] = dic.get(child, []) + [(parent, length)]
    visited[1] = True
    a = bfs(1)[0]
    visited = [False] * (n+1)
    visited[a] = True
    print(bfs(a)[1])