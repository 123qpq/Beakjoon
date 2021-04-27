import sys
n, m = map(int, sys.stdin.readline().split())
temp = list(map(int, sys.stdin.readline().split()))
if temp[0] == 0:
    print(m)
    sys.exit(0)
else:
    temp = set(temp[1:])
    party = []
    party2 = []
    for _ in range(m):
        set1 = set(list(map(int, sys.stdin.readline().split()))[1:])
        if len(set1 & temp) == 0:
            party.append(set1)
        else:
            temp |= set1
    
    for _ in range(m-1):
        for p in party:
            if len(p & temp) == 0:
                party2.append(p)
            else:
                temp |= p
        if len(party2) == 0:
            break
        party = party2
        party2 = []
    
    print(len(party))