#16947
import sys
sys.setrecursionlimit(100000)

def find_cicle(node, before): #사이클 찾기
    global ciclenode
    if node in cicle:
        ciclenode = node
        return True
    else:
        for n in subway[node]:
            if n != before:
                cicle.append(node)
                if find_cicle(n, node):
                    return True
                cicle.pop()

def search(level, node, befor): #사이클 아닌 노드들 탐색
    for n in subway[node]:
        if n != befor:
            res[n-1] = level
            search(level+1, n, node)

n = int(input())
subway = {}
for _ in range(n): #트리 생성
    a, b = map(int, input().split())
    subway[a] = subway.get(a, []) + [b]
    subway[b] = subway.get(b, []) + [a]

cicle = []
uncicle = []
res = [0]*max(subway)
ciclenode = 1
find_cicle(1, 0)

if ciclenode != 1: # 순수 사이클만 남겨둠
    nownode = 1
    while ciclenode != nownode:
        cicle.pop(0)
        nownode = cicle[0]

for idx in range(len(res)): # 나머지 간선들 거리 측정
    if idx+1 in cicle:
        continue
    else:
        for now in subway[idx+1]:
            if now in cicle:
                uncicle.append(idx+1)
                res[idx] = 1
                search(2, idx+1, now)
print(' '.join(map(str, res)))
