from collections import Counter
file = open('Days of Advent Code\Day 7\input.txt','r')

s = []
order = [str(x) for x in ['A', 'K', 'Q', 'J', 'T', 9, 8, 7, 6, 5, 4, 3, 2]]
order = order[::-1]

cards = []
dic = {}
for line in file.readlines():
    card,bid = line.split()
    c = Counter(card)
    cards.append((card,c.most_common()[0][1],c.most_common()[1][1] if len(c)> 1 else 0))
    dic[card] = int(bid)

cards = sorted(cards, key=lambda card:(card[1],card[2],[order.index(c) for c in card[0]]))
ans = 0

for i,x in enumerate(cards):
    ans += (i+1)*dic[x[0]]

print(ans)
