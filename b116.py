H, W, T = map(int, input().split())

# 男性と女性が持っているプレゼントの初期状態
men_gifts = [('M', i) for i in range(1, H+1)]
women_gifts = [('F', i) for i in range(1, W+1)]
# 男性と女性の初期座標
men_pos = [(i,0) for i in range (1, H+1)]
women_pos = [(0,j) for j in range(1, W+1)]

for t in range(1,T+1):
    # 男性の時間tの座標
    men_t = t % (2*W)
#    print(t)
    if men_t > W:
        men_t = 2*W - men_t
    men_pos = [(i,men_t) for i in range(1, H+1)]
#    print(men_pos)
    # 女性の時間tの座標
    women_t = t % (2*H)
    if women_t > H:
        women_t = 2*H - women_t
    women_pos = [(women_t, j) for j in range(1, W+1)]
#    print(women_pos)

# それぞれの男女が同じ座標であればプレゼントを交換する
    for r in range(H):
#        print(men_pos[r])
        for c in range(W):
#            print(women_pos[c])
            if men_pos[r] == women_pos[c]:
                men_gifts[r],women_gifts[c] = women_gifts[c],men_gifts[r]

#    print(t)
#    print(men_gifts)
#    print(women_gifts)

# 出力
for gift in men_gifts:
    print(gift[0], gift[1])
for gift in women_gifts:
    print(gift[0], gift[1])