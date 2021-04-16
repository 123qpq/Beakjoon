import sys
sys.setrecursionlimit(1000000)
n = int(input()) #전위순회 구하기
inorder = list(map(int, input().split())) #중위순회
postorder = list(map(int, input().split())) #후위순회

def search(inod, postod):
    root = postod[-1]
    pv = inod.index(root)
    n = len(inod)
    if n <= 3:
        if inod != postod:
            inod[0], inod[1] = inod[1], inod[0]
        for i in inod:
            print(i, end = ' ')
    else:
        print(root, end = ' ')
        search(inod[:pv], postod[:pv])
        search(inod[pv+1:], postod[pv:-1])

search(inorder, postorder)


'''
재귀 사용
후위의 마지막노드를 루트노드로 가져옴
전위 후위 순회
전위의 노드가 루트노드랑 같아지면 자른다


중위 특
가장 왼쪽노드
root 전까지는 왼쪽노드

후위 특
가장 왼쪽노드
가장 마지막에 root
'''

