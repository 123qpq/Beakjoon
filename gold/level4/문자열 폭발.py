#9935
import sys

string = sys.stdin.readline().rstrip()
bomb = list(sys.stdin.readline().rstrip())
b = len(bomb)
last = bomb[-1]
stack = []
for s in string:
    stack.append(s)
    if s == last and stack[-b:] == bomb:
        del stack[-b:]
if stack:
    print(''.join(stack))
else:
    print("FRULA")