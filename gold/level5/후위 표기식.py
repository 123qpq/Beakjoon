#1918
import sys
line = sys.stdin.readline()
answer = ''
sign = {"+" : 1, '-' : 1, '*' : 2, '/' : 2, '(' : 0}
stack = []
for l in line[:-1]:
    if l.isalpha():
        answer += l
    elif l == '(':
        stack.append(l)
    elif l == ')':
        while stack[-1] != '(':
            answer += stack.pop()
        stack.pop()
    else:
        while stack and sign[l] <= sign[stack[-1]]:
            answer += stack.pop()
        stack.append(l)
while stack:
    answer += stack.pop()
print(answer)