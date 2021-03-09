#2003
from collections import deque
n, m = map(int, input().split())
lst = list(map(int, input().split()))
temp = deque()
cnt = 0
for i in range(n):
    temp.append(lst[i])
    while m < sum(temp):
        temp.popleft()
    if sum(temp) == m:
        cnt +=1
        temp.popleft()
print(cnt)