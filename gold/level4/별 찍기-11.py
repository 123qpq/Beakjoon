#2448
import math
    
s = ["  *   ", " * *  ", "***** "]

def Star(shift):
    c = len(s)
    for i in range(c):
        s.append(s[i] + s[i])
        s[i] = ("   " * shift + s[i] + "   " * shift)
        
n = int(input())
k = int(math.log(int(n/3), 2))
for i in range(k):
    Star(int(pow(2, i)))

print('\n'.join(s))