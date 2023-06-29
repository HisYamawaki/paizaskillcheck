n,m = map(int,input().split())
seiseki = 0

for i in range(1,n+1):
    a,b = map(int,input().split())
    seiseki = a- 5*b
    if seiseki <= 0:
        seiseki = 0
    if seiseki >= m:   
        print(i)

