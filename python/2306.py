N = int(input()) #Número de colunas
colunas = input().split()

pedrasTotais = 0
for ele in colunas: pedrasTotais+=int(ele)

escada = int(N*(N+1)/2)
pedrasBase= pedrasTotais - escada
alturaBase = int(pedrasBase//N)

if alturaBase >= 0 and pedrasBase >= 0 and (pedrasBase%N) == 0:
    pedrasSobrando = 0 #Pedras que sobram em cada coluna
    mudanca = 0 #quantidade de mudanças
    c = 1 #Quantidade de pedras que tem na coluna acima da base 
    for col in colunas:
        col = int(col)
        dt = alturaBase + c #quantidade de pedras que deveriam ter
        if col == dt: pass
        elif col > dt: #Tem pedras de mais, há mudança.
            pedrasSobrando += col - dt
            mudanca += col - dt
        else: #Tem pedras de menos.
            pedrasSobrando -= dt - col
        c += 1
else:
    pedrasSobrando = 1

if pedrasSobrando == 0:
    print(mudanca)
else:
    print(-1)
