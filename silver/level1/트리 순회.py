#1991
def bfs(level, node):
    if level == n:
        print()
    else:
        lt = graph[node][0]
        rt = graph[node][1]
        res1.append(node)
        if lt != '.':
            bfs(level+1, lt)
        res2.append(node)
        if rt != '.':
            bfs(level+1, rt)
        res3.append(node)

n = int(input())
graph = {}
for i in range(n):
    root, left, right = input().split()
    graph[root] = [left, right]
res1 = [] # 전위
res2 = [] # 중위
res3 = [] # 후위
bfs(0, 'A')
print(''.join(res1))
print(''.join(res2))
print(''.join(res3))