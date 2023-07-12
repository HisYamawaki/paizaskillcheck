n,k = map(int,input().split())
tlst =[]

for i in range(n):
    a = int(input())
    tlst.append(a)

tlst = sorted(tlst)

min_diff = float('inf')

for j in tlst:
    diff = abs(j - k)
    if diff < min_diff:
        min_diff = diff
        result = [j]
    elif diff == min_diff:
        result.append(j)

for i in result:
    print(i)