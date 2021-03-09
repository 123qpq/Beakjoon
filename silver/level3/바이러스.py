#2606
n = int(input())
c = int(input())
dic = {}
visited = [False]*(n+1)
for _ in range(c):
    x, y = map(int, input().split())
    dic[x] = dic.get(x, []) + [y]
    dic[y] = dic.get(y, []) + [x]

stack = [1]
while stack:
    now = stack.pop()
    for n in dic[now]:
        if visited[n] == False:
            stack.append(n)
            visited[n] = True
print(visited.count(True)-1)