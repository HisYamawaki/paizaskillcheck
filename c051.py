a,b,c,d = map(int,input().split())

card = [a,b,c,d]
card = sorted(card)

max1 = 10*card[3] + 10*card[2] + card[1] + card[0]

print(max1)