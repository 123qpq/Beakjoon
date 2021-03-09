#1620
import sys
n, m = map(int, sys.stdin.readline().split())
lst = []
dic = {}
for i in range(n):
    pocket = sys.stdin.readline().rstrip()
    lst.append(pocket)
    dic[pocket] = i+1
for _ in range(m):
    temp = sys.stdin.readline().rstrip()
    if temp.isdigit():
        print(lst[int(temp)-1])
    else:
        print(dic[temp])