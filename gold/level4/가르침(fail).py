#fail
from itertools import combinations
import sys



n, k = map(int, input().split())
if k < 5 or k == 26:
    print(0 if k < 5 else n)
    sys.exit()
base = ['a', 'n', 't', 'i', 'c']
table = [False]*21

alpha = []
words = []
res = 0
for i in range(n):
    temp = input()[4:-4]
    words.append(temp)
    for t in temp:
        if t not in base:
            if t not in alpha:
                alpha.append(t)
print(words)
if len(alpha) < k-5:
    print(n)
else:
    for check in list(combinations(alpha, k-5)):
        for c in check:
            table[ord(c) - ord('a')] = True
            cnt = 0
        for word in words:
            for w in word:
                print(w)
                if w in base:
                    continue
                if [ord(w) - ord('a')] == True:
                    continue
                break
            else:
                cnt += 1
        if res < cnt:
            res = cnt
        for c in check:
            table[ord(c) - ord('a')] = False

    print(res)
