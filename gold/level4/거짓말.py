import sys
n, m = map(int, sys.stdin.readline().split())
temp = list(map(int, sys.stdin.readline().split()))
if temp[0] == 0:
    print(m)
else:
    temp = set(temp[1:])
    party = []
    party2 = []
    for _ in range(m):
        set1 = list(map(int, sys.stdin.readline().split()))[1:]
        if len(set(set1) & temp) == 0:
            party.append(set(set1))
        else:
            temp |= set(set1)
    
    for _ in range(m-1):
        for p in party:
            if len(p & temp) == 0:
                party2.append(p)
            else:
                temp |= p
        party = party2
        party2 = []
    
    print(len(party))