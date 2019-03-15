nbSymByCard = 12
nbCards = (nbSymByCard**2) - nbSymByCard + 1
cards = []
n = nbSymByCard - 1
t = []
t.append([[(i+1)+(j*n) for i in range(n)] for j in range(n)])
for ti in range(n-1):
  t.append([[t[0][((ti+1)*i) % n][(j+i) % n] for i in range(n)] for j in range(n)])
t.append([[t[0][i][j] for i in range(n)] for j in range(n)])
for i in range(n):
  t[0][i].append(nbCards - n)
  t[n][i].append(nbCards - n + 1)
  for ti in range(n-1):
    t[ti+1][i].append(nbCards - n + 1 + ti + 1)
t.append([[(i+(nbCards-n)) for i in range(nbSymByCard)]])
for ti in t:
  cards = cards + ti
print cards
