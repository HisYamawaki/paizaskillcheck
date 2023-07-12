n,m = map(int,input().split())
chg = n
pt = 0

for i in range(m):
    fare = int(input())
    if pt >= fare:
        pt -= fare
        print(chg, pt)
    else:
        chg -= fare
        pt = int(pt + 0.1*fare)
        print(chg, pt)
