n,a,b = map(int, input().split())

for i in range(1, n+1):
    if i%a == 0 and i%b == 0:
        print("AB")
    elif i%a == 0:
        print("A")
    elif i%b == 0:
        print("B")
    else:
        print("N")
