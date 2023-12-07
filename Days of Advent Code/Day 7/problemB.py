from collections import Counter
file = open('Days of Advent Code\Day 7\input.txt','r')

order = [str(x) for x in ['A', 'K', 'Q', 'T', 9, 8, 7, 6, 5, 4, 3, 2, 'J']]
order = order[::-1]

dic = {}
cards = []
for line in file.readlines():
    card,bid = line.split()
    c = Counter(card)
    x = c.most_common()[0][0]
    if 'J' !=  x:
        c[x] += c['J']
        del c['J']
    elif len(c) != 1:
        x = c.most_common()[1][0]
        c[x] += c['J']
        del c['J']
    cards.append((card,c.most_common()[0][1] if len(c) != 0 else 5,c.most_common()[1][1] if len(c)> 1 else 0))
    dic[card] = int(bid)

cards = sorted(cards, key=lambda card:(card[1],card[2],[order.index(c) for c in card[0]]))

ans = 0
for i,x in enumerate(cards):
    ans += (i+1)*dic[x[0]]

print(ans)
