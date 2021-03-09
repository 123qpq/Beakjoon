#10954
import sys
import bisect
from collections import deque

for _ in range(int(sys.stdin.readline())):
    q = deque()
    dic = {}
    for _ in range(int(sys.stdin.readline())):
        temp = sys.stdin.readline().split()
        id = temp[0]
        num = int(temp[1])
        if id == 'I':
            if num not in dic: #같은 값이 존재하지 않으면
                dic[num] = 1
                bisect.insort_left(q, num)
            else: #같은 값이 존재하면
                dic[num] += 1
        elif q: #id = 'D' 이면서 q 가 있으면
            if num == 1:
                if dic.get(q[-1]) == 1:
                    dic.pop(q[-1])
                    q.pop()
                else:
                    dic[q[-1]] -= 1
            else:
                if dic.get(q[0]) == 1:
                    dic.pop(q[0])
                    q.popleft()
                else:
                    dic[q[0]] -= 1
    if dic:
        print(q[-1], q[0])
    else:
        print('EMPTY')