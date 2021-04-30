#2263
import sys
sys.setrecursionlimit(1000000)
n = int(input()) #전위순회 구하기
inorder = list(map(int, input().split())) #중위순회
postorder = list(map(int, input().split())) #후위순회

pos = [0] * (n+1)
for i in range(n):
    pos[inorder[i]] = i

def search(in_start, in_end, po_start, po_end):
    if (in_start > in_end) or (po_start > po_end):
        return
    
    root = postorder[po_end]
    print(root, end = " ")
    
    left = pos[root] - in_start
    right = in_end - pos[root]

    search(in_start, in_start+left-1, po_start, po_start+left-1)
    search(in_end-right+1, in_end, po_end-right, po_end-1)

search(0, n-1, 0, n-1)

'''
재귀 사용
후위의 마지막노드를 루트노드로 가져옴
전위 후위 순회
루트 출력, 전위, 후위 순으로 진행


중위 특
가장 왼쪽노드
root 전까지는 왼쪽노드

후위 특
가장 왼쪽노드
가장 마지막에 root
'''

