n,m = map(int,input().split())
a = input()
kuji = list(map(int, a.split()))

for i in range(n - m +1):
    if sum(kuji[i:i+m]) == 0:
        print("NG")
        break
else:
    print("OK")