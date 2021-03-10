#1167
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
    dic = {}
    visited = [False] * (n+1)
    ans = 0

    for _ in range(n):
        node, *temp = map(int, sys.stdin.readline().split())
        for i in range(0, len(temp)-1, 2):
            dic[node] = dic.get(node, []) + [(temp[i], temp[i+1])]

    visited[1] = True
    a = bfs(1)[0]
    visited = [False] * (n+1)
    visited[a] = True
    print(bfs(a)[1])