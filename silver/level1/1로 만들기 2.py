#12852
from collections import deque
n = int(input())
if n == 1:
    print(0)
    print(1)
count = 0
check = [False]*(n+1)
que = deque()
que.append([1])

while que:
    count += 1
    for _ in range(len(que)):
        deep = que.popleft()
        num = deep[0]
        if num + 1 == n or num * 3 == n or num * 2 == n:
            print(count)
            print(' '.join(str(_) for _ in [n]+deep))
            exit(0)
        for i in [num*3, num*2, num+1]:
            if i < n and check[i] == False:
                que.append([i]+deep)
                check[i] = True
