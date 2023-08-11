H, W = map(int, input().split())
S = [input() for i in range(H)]
y, x = map(int, input().split())

if S[y][x] == '.':
    S[y] = S[y][:x] + '#' + S[y][x+1:]
else:
    S[y] = S[y][:x] + '.' + S[y][x+1:]

for val in S:
    print(val)