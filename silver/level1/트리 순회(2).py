#1991
def bfs1(level, node):
    if node == '.':
        return
    res1.append(node)
    bfs1(level+1, graph[node][0])
    bfs1(level+1, graph[node][1])

def bfs2(level, node):
    if node == '.':
        return
    bfs2(level+1, graph[node][0])
    res2.append(node)
    bfs2(level+1, graph[node][1])

def bfs3(level, node):
    if node == '.':
        return
    bfs3(level+1, graph[node][0])
    bfs3(level+1, graph[node][1])
    res3.append(node)

n = int(input())
graph = {}
for i in range(n):
    root, left, right = input().split()
    graph[root] = [left, right]
res1 = [] # 전위
res2 = [] # 중위
res3 = [] # 후위
bfs1(0, 'A')
bfs2(0, 'A')
bfs3(0, 'A')
print(''.join(res1))
print(''.join(res2))
print(''.join(res3))