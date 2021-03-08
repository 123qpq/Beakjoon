#16928
import sys
from collections import deque
l, s = map(int, input().split())
visited = [True] * 101
game = [0] * 101

for _ in range(l+s):
    start, end = map(int, sys.stdin.readline().split())
    game[start] = end

goto = deque() 
goto.append((1, 0))#1번부터 시작
while goto:
    now = goto.popleft()
    if now[0] == 100: #100이 되면 출력함. bfs 이므로 가장빨리 찾은 답이 가장 빠른 답
        print(now[1])
        sys.exit()
    for i in range(1, 7): #1~6까지 굴리기
        next = now[0] + i
        if 100 < next: #100 이상은 넘어감
            continue
        if game[next] != 0: #사다리나 뱀의 경우
            next = game[next] # 그 값을 넣어줌
        if visited[next]: #밟은적이 없을 경우
            visited[next] = False
            goto.append((next, now[1]+1))

'''

아래의 코드는 22퍼에서 오류가 발생하는데 왜 틀렸는지 모르겠음

import sys
from collections import deque
l, s = map(int, input().split())
jump = {}
game = [0, 0] + [float('inf')] * 99

for _ in range(l+s):
    start, end = map(int, sys.stdin.readline().split())
    jump[start] = end

goto = deque([1]) #1번부터 시작
while goto:
    now = goto.popleft()
    if now == 100: #100이 되면 출력함. bfs 이므로 가장빨리 찾은 답이 가장 빠른 답
        print(game[-1])
        sys.exit()
    for i in range(1, 7): #1~6까지 굴리기
        next = now + i
        if 100 < next: #100 이상은 넘어감
            continue
        if next in jump and jump[next] != 0 and game[now]+1 < game[jump[next]]: #다음 값이 사다리나 뱀이고 0으로 가지 않고 기존 값보다 작아야함
            game[jump[next]] = game[now]+1
            game[next] = -1 #밟았다는 증거
            goto.append(jump[next]) #밟은 값 추가
        elif game[now]+1 < game[next]: #그냥 앞으로 가는 경우 역시 기존 값보다 작아야함
            game[next] = game[now]+1
            goto.append(next)
'''