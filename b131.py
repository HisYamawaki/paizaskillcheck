N,M = map(int, input().split())

A = [list(map(int, input().split())) for i in range(N)]
X = int(input())

route = [tuple(map(int, input().split())) for j in range(X)]

#print(A)
#print(route)

#routeを経由した際の運賃を計算するには、以下のようなロジックを実装することができます。

fare = 0
current_line = 1
current_station = 1

for line, station in route:
    if current_line == line:
        fare += abs(A[line-1][station-1] - A[line-1][current_station-1])
    else:
        fare += abs(A[line-1][station-1] - A[line-1][current_station-1])
    current_line = line
    current_station = station

#line = 3
#station = 2
#if current_line == line:
#    fare += abs(A[line-1][station-1] - A[line-1][current_station-1])
#else:
#    fare += abs(A[line-1][station-1] - A[line-1][current_station-1])
    

print(fare)