N,T = input().split()
N, T = int(N), int(T)
Mpv = [[],[]] #Matriz de peso e e valores

for i in range(0,N):
    C,V = input().split()
    C,V = int(C), int(V)
    Mpv[0].append(C)
    Mpv[1].append(V)

Matriz_principal=[] 
for e in range(N+1):
    Matriz_principal.insert(e,[0])
    for l in range(T):
        Matriz_principal[e].insert(l,0)

#percorre a matriz principal
for col in range(1,T+1):
    cano = col
    for lin in range(1,N+1):
        tamanho_corte = Mpv[0][lin-1] 
        if cano < tamanho_corte:
            ele = Matriz_principal[lin-1][col]

            Matriz_principal[lin][col] = ele

        else:
            p = Mpv[0][lin-1]
            v = Mpv[1][lin-1]

            ele = max(Matriz_principal[lin-1][col],Matriz_principal[lin][col-p]+v)

            Matriz_principal[lin][col] = ele

print(Matriz_principal[-1][-1])