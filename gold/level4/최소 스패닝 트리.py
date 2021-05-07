#1197
import sys
v, e = map(int, sys.stdin.readline().split())
uniset = [i for i in range(v+1)]
network = [list(map(int, sys.stdin.readline().split())) for _ in range(e)]
network.sort(key = lambda x: x[2])
answer = 0

def find(node):
    if node != uniset[node]: #부모 노드 찾기
        uniset[node] = find(uniset[node])
    return uniset[node]

def union(no1, no2): #하나의 집합으로 연결
    root1 = find(no1)
    root2 = find(no2)
    uniset[root1] = root2

for net in network:
    if find(net[0]) != find(net[1]): #다른 집합이면 합치기
        union(net[0], net[1])
        answer += net[2]
print(answer)