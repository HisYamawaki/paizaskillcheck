n,d = map(int,input().split())
lng = d


for i in range(n-1):
    a = int(input())
    lng += d - a

print(d*lng)